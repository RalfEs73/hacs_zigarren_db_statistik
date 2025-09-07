# Zigarren DB Statistik – Home Assistant Integration
Diese benutzerdefinierte Integration für Home Assistant erstellt einen Sensor, der Statistiken aus der Zigarren-Datenbank.

## 🧾 Beschreibung
Der Sensor `sensor.zigarren_db_statistik` zeigt die Anzahl der Zigarren auf Lager als Hauptwert an und stellt weitere Informationen als Attribute bereit.


## ⚙️ Installation
Füge die einzelnen Humidore manuell in deiner `configuration.yaml` hinzu:

```yaml
sensor:
    - platform: zigarren_db_statistik
```

