# homeassistant-custom-components
My own custom components for Home Assistant


## AEMET Sensor

Sensor support for AEMET (Agencia Estatal de Metereología) data service.

You need to get your "api_key" and find the nearest "station_id"
at https://opendata.aemet.es/

```
# configuration.yaml
sensor:
  - platform: aemet
    name: AEMET
    api_key: !secret aemet_api_key
    station_id: !secret aemet_station_id
    monitored_conditions:
      - temperature
      - humidity
      - pressure
      - precipitation
      - snow
      - visibility
      - wind_speed
```
