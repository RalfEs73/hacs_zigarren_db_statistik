import requests
import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

API_URL = "https://zigarren-db.de/api/ha_statistik_test.php"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setzt die Plattform für den Zigarren DB Sensor."""
    add_entities([ZigarrenDBSensor()], True)

class ZigarrenDBSensor(Entity):
    """Repräsentiert den Zigarren DB Statistik Sensor."""

    def __init__(self):
        self._state = None
        self._attributes = {}

    def update(self):
        """Aktualisiert die Sensordaten durch Abruf der API."""
        try:
            response = requests.get(API_URL, timeout=10)
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