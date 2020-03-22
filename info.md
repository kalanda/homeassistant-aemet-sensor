# AEMET Sensor

Sensor support for AEMET (Agencia Estatal de Metereología) weather data service of Spain.

You need to get your `api_key` and find the nearest `station_id` at https://opendata.aemet.es/
in order to finish the configuration.

**IMPORTANT NOTE: You have to get the `station_id` from "Observación convencional" => "Datos de observación" stations. It isn't the same that in "Climatologías diarias".**

**IMPORTANT NOTE 2: Don't forget to use double quotes (`"` and `"`) around `name`, `api_key` and `station_id` values**

## Add to your configuration.yaml

```
sensor:
  - platform: aemet
    name: "AEMET"
    api_key: "[ YOUR_AEMET_API_KEY ]"
    station_id: "[ YOUR_AEMET_STATION_ID ]"
    monitored_conditions:
      - temperature
      - humidity
      - pressure
      - precipitation
      - snow
      - visibility
      - wind_speed
      - wind_max_speed
      - wind_bearing
```

You can also configure the component as a weather service.

```
weather:
  - platform: aemet
    name: "AEMET"
    api_key: "[ YOUR_AEMET_API_KEY ]"
    station_id: "[ YOUR_AEMET_STATION_ID ]"
```

*Please*, note that because of how AEMET is retrieving the data, the weather component can't show you the current condition (sunny, cloudy, ...) and neither the forecast, just current values for weather sensors.