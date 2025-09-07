import requests
import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

BASE_URL = "https://zigarren-db.de/api/ha_statistik_test2.php"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setzt die Plattform für den Zigarren DB Sensor."""
    api_param = config.get("api", "")
    full_url = f"{BASE_URL}?api={api_param}" if api_param else BASE_URL
    add_entities([ZigarrenDBSensor(full_url)], True)

class ZigarrenDBSensor(Entity):
    """Repräsentiert den Zigarren DB Statistik Sensor."""

    def __init__(self, api_url):
        self._api_url = api_url
        self._state = None
        self._attributes = {}

    def update(self):
        """Aktualisiert die Sensordaten durch Abruf der API."""
        try:
            response = requests.get(self._api_url, timeout=10)
            data = response.json()
            self._state = data.get("auf_lager")
            self._attributes = {k: v for k, v in data.items() if k != "auf_lager"}
        except Exception as e:
            _LOGGER.error("Fehler beim Abrufen der Zigarren-Statistik: %s", e)

    @property
    def name(self):
        return "Zigarren DB Statistik"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    @property
    def icon(self):
        return "mdi:cigar"