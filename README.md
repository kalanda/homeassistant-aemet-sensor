[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

```
IMPORTANT NOTE:
Home Assistant now has native support for AEMET, so I've decided to stop this component development.

NOTA IMPORTANTE:
Home Assistant ahora soporta AEMET de forma nativa, así que he decidido dejar de evolucionar este componente.
```

https://www.home-assistant.io/integrations/aemet/

---

# AEMET Sensor

Sensor support for AEMET (Agencia Estatal de Metereología) weather data service of Spain.

You need to get your `api_key` and find the nearest `station_id` at https://opendata.aemet.es/
in order to finish the configuration.

**IMPORTANT NOTE: You have to get the `station_id` from "Observación convencional" => "Datos de observación" stations. **NOT** from "Climatologías diarias".**

**IMPORTANT NOTE 2: Don't forget to use double quotes (`"` and `"`) around `name`, `api_key` and `station_id` values**

Install is available using [HACS](https://github.com/custom-components/hacs) or you can install manually.

## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `aemet`.
4. Download _all_ the files from the `custom_components/aemet/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.

You need to get your "api_key" and find the nearest "station_id" at https://opendata.aemet.es/
in order to finish the configuration.

## Example configuration.yaml

```
sensor:
  - platform: aemet
    name: "AEMET"
    api_key: "YOUR_AEMET_API_KEY"
    station_id: "YOUR_AEMET_STATION_ID"
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
    api_key: "YOUR_AEMET_API_KEY"
    station_id: "YOUR_AEMET_STATION_ID"
```

*Please*, note that because of how AEMET is retrieving the data, the weather component can't show you the current condition (sunny, cloudy, ...) and neither the forecast, just current values for weather sensors.
