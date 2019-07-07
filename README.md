[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

# AEMET Sensor

Sensor support for AEMET (Agencia Estatal de Metereología) weather data service.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `aemet`.
4. Download _all_ the files from the `custom_components/aemet/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.

You need to get your "api_key" and find the nearest "station_id" at https://opendata.aemet.es/
in order to finish the configuration.

## Example configuration.yaml

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
