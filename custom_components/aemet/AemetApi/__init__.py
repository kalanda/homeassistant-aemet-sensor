import requests
from datetime import timedelta
from logging import getLogger
from homeassistant.util import Throttle

_LOGGER = getLogger(__name__)

from homeassistant.components.weather import (
    ATTR_WEATHER_HUMIDITY, ATTR_WEATHER_PRESSURE, ATTR_WEATHER_TEMPERATURE,
    ATTR_WEATHER_VISIBILITY)
from homeassistant.const import (
    ATTR_LATITUDE, ATTR_LONGITUDE, HTTP_OK)

ATTR_ELEVATION = 'elevation'
ATTR_LAST_UPDATE = 'last_update'
ATTR_STATION_NAME = 'station_name'
ATTR_WEATHER_PRECIPITATION = 'precipitation'
ATTR_WEATHER_SNOW = 'snow'
ATTR_WEATHER_WIND_SPEED = 'wind_speed'

CONF_ATTRIBUTION = 'Data provided by AEMET'
CONF_STATION_ID = 'station_id'

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)

class AemetApi:
    """Get the lastest data and updates the states."""
    API_URL_BASE = 'https://opendata.aemet.es/opendata/api'
    API_STATION_ENDPOINT = '/observacion/convencional/datos/estacion/{}'

    def __init__(self, api_key, station_id):
        """Initialize the data object."""
        self._station_id = station_id
        self._api_key = api_key
        self.data = {}

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Fetch new state data for the sensor."""
        _LOGGER.debug("------- Updating AEMET sensor")

        endpoint_url = "{}{}".format(
                            self.API_URL_BASE,
                            self.API_STATION_ENDPOINT.format(self._station_id)
                        )
        params = {'api_key': self._api_key}
        main_rsp = requests.get(endpoint_url, params=params)
        if main_rsp.status_code != HTTP_OK:
            _LOGGER.error("Invalid response: %s", main_rsp.status_code)
            return

        main_result = main_rsp.json()
        if main_result['estado'] == HTTP_OK:
            hashed_endpoint = main_result["datos"]
            data_rsp = requests.get(hashed_endpoint)
            if data_rsp.status_code != HTTP_OK:
                _LOGGER.error("Invalid response: %s", data_rsp.status_code)
            data_result = data_rsp.json()
            last_update = data_result[-1]
            self.set_data(last_update)
            _LOGGER.debug(last_update)
        else:
            _LOGGER.error("Invalid response: %s", main_rsp.status_code)

    def set_data(self, record):
        """Set data using the last record from API."""
        state = {}
        if 'lon' in record:
            state[ATTR_LONGITUDE] = record['lon']
        if 'lat' in record:
            state[ATTR_LATITUDE] = record['lat']
        if 'alt' in record:
            state[ATTR_ELEVATION] = record['alt']
        if 'ubi' in record:
            state[ATTR_STATION_NAME] = record['ubi']
        if 'prec' in record:
            state[ATTR_WEATHER_PRECIPITATION] = record['prec']
        if 'pres' in record:
            state[ATTR_WEATHER_PRESSURE] = record['pres']
        if 'ta' in record:
            state[ATTR_WEATHER_TEMPERATURE] = record['ta']
        if 'hr' in record:
            state[ATTR_WEATHER_HUMIDITY] = record['hr']
        if 'fint' in record:
            state[ATTR_LAST_UPDATE] = record['fint']
        if 'vis' in record:
            state[ATTR_WEATHER_VISIBILITY] = record['vis']
        if 'nieve' in record:
            state[ATTR_WEATHER_SNOW] = record['nieve']
        if 'vv' in record:
            state[ATTR_WEATHER_WIND_SPEED] = record['vv']
        self.data = state

    def get_data(self, variable):
        """Get the data."""
        return self.data.get(variable)