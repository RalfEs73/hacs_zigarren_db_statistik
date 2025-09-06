# Zigarren DB Statistik – Home Assistant Integration

Diese benutzerdefinierte Integration für Home Assistant erstellt einen Sensor, der Statistiken aus der Zigarren-Datenbank unter [zigarren-db.de](https://ruft.

## 🧾 Beschreibung

Der Sensor `sensor.zigarren_db_statistik` zeigt die Anzahl der Zigarren auf Lager als Hauptwert an und stellt weitere Informationen als Attribute bereit.

### 🔍 API-Quelle

Die Daten werden von folgender API bezogen:  
`https://zigarren-db.de/api/ha_statistik_test.php`

### 📊 Sensor-Daten

- **Wert (`state`)**: `auf_lager` – Anzahl der Zigarren auf Lager
- **Attribute**:
  - `alle_zigarren_preis`
  - `alle_zigarren_schnitt_preis`
  - `zigarren_add`
  - `zigarren_msg`
  - `letzte_zigarre_id`
  - `letzte_zigarre_datum`
  - `letzte_zigarre`
  - `letzte_zigarre_bild_url`

## ⚙️ Installation

1. Kopiere den Ordner `hacs_zigarren_db_statistik` in dein Home Assistant Verzeichnis unter `custom_components`.
2. Füge folgenden Eintrag in deine `configuration.yaml` ein:


sensor:
  - platform: hacs_zigarren_db_statistik
