# serverueberwachung
 EVP-Projekt Serverueberwachung
 Projekt von Annika, Jan, Oliver und Justin

 Hercules-Tool für Testen der Verbindungen => https://www.hw-group.com/software/hercules-setup-utility
 nach Installation den Reiter TCP-Server auswählen, als IP dann im Programm den localhost 127.0.0.1 und Port in dem Tool eintragen
 danach kann die Verbindung hergestellt werden und das Programm funktioniert auch ohne Connection.

## Mögliche ToDo's & Überlegungen:
- Globale Variable einführen, welche dann keine Connection mehr aufbaut (offlinemodus mit ggfs. Simulationsdaten)
- Disconnect der einzelnen Bricklets mit einem finally im jedem Fall schliessen
- Abfragereihenfolge für PORT und HOST umverlagern (In Tests wollte PORT und HOST aus uid_list.py geholt werden, bevor der Konsolencommand für die Abfrage lief)