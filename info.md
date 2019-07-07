# AEMET Sensor

Sensor support for AEMET (Agencia Estatal de Metereología) weather data service of Spain.

You need to get your `api_key` and find the nearest `station_id` at https://opendata.aemet.es/
in order to finish the configuration.

## Add to your configuration.yaml

```
sensor:
  - platform: aemet
    name: AEMET
    api_key: [ YOUR_AEMET_API_KEY ]
    station_id: [ YOUR_AEMET_STATION_ID ]
    monitored_conditions:
      - temperature
      - humidity
      - pressure
      - precipitation
      - snow
      - visibility
      - wind_speed
```
