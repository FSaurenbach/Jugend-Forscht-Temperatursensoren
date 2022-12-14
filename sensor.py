#!/usr/bin/env python
import time  # Modul um das Programm für eine Bestimmte Zeit zu stoppen.
from datetime import datetime  # Modul um die aktuelle Zeit auszulesen.


def is_time():  # Funktion, die alle 5 Minuten die Daten ausliest.
    current_minute = datetime.now().strftime("%M")  # Die aktuelle Minute auslesen als Variable abspeichern.
    if "0" in current_minute or "5" in current_minute:  # Wenn eine 5 oder 0 in der aktuellen Minute ist, z.B 20 oder 25, Funktion richtig setzen.
        return True
    else:  # Wenn keine 5 oder 0 in der aktuellen Minute ist die Funktion Falsch setzen
        return False


sensor1 = "/sys/bus/w1/devices/28-3c01f0960400/w1_slave"  # Variablen vom Dateipfad der Sensoren
sensor2 = "/sys/bus/w1/devices/28-3c01f096db57/w1_slave"
f = open(sensor1, "r")  # Auf beide Sensoren zugreifen mit der open() Funktion.
f2 = open(sensor2, "r")

sensor1_text = open("Sensor1.txt",
                    "a")  # Datenbanken für die jeweiligen Temperaturwerte öffnen. "a" steht hier für "append" also Werte der Datei hinzufügen.
sensor2_text = open("Sensor2.txt", "a")

while True:  # Dauerschleife um alle 20 Sekunden zu überprüfen ob es Zeit ist Messungen zu machen(Funktion is_time())
    if is_time():  # Wenn es Zeit ist: Temperatur auslesen und speichern

        data = open(sensor1, "r").read()  # Auf beide Sensoren erneut zugreifen um aktuelle Temperatur zu bekommen.
        data2 = open(sensor2, "r").read()
        (discard, sep, reading) = data.partition(' t=')  # Nur die Temperatur herausfiltern aus den Daten
        t = float(reading) / 1000.0  # Temperatur umrechenen
        with open("Sensor1.txt", "a") as f:  # Datenbank öffnen und Temperatur spreichern.
            f.write("\n")
            now = datetime.now()
            current_minute = now.strftime("%H:%M")  # Die aktuelle Zeit zu den Temperaturdaten hinzufügen
            f.write(current_minute + " ," + str(t))  # Abspeichern der daten

        # Gleiches Vorgehen
        (discard, sep, reading) = data2.partition(' t=')
        t = float(reading) / 1000.0
        print("Sensor 2 {:.1f}".format(t))
        with open("Sensor2.txt", 'a') as f:
            f.write("\n")
            now = datetime.now()
            current_minute = now.strftime("%H:%M")
            f.write(current_minute + " ," + str(t))

        time.sleep(120)  # 120 Sekunden warten um zwei Messungen auf einmal zu verhindern
    else:
        time.sleep(20)  # 20 Sekunden warten um den RaspberryPi nicht zu überlasten.
