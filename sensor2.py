#!/usr/bin/env python
from datetime import datetime  # Zeit modul um festzulegen wie oft messungen gemacht werden
import time


def is_time(): # Alle 30 Minuten die Daten auslesen.
    return True
    now = datetime.now()
    current_minute = now.strftime("%M")
    print(current_minute)
    if current_minute == "30" or current_minute == "00":
        print("fa")
        return True
    else:
        return False


sensor1 = "/sys/bus/w1/devices/28-3c01f0960400/w1_slave"  # Sensor 1
sensor2 = "/sys/bus/w1/devices/28-3c01f096db57/w1_slave"  # Sensor 2
f = open(sensor1, "r")  # Auf beide Sensoren zugreifen
f2 = open(sensor2, "r")

sensor1_text = open("Sensor1.txt", "a")
sensor2_text = open("Sensor2.txt", "a")

data = f.read()  # Die Daten auslesen
data2 = f2.read()
while True:
    if is_time():
        f = open(sensor1, "r")  # Auf beide Sensoren zugreifen
        f2 = open(sensor2, "r")
        data = f.read()
        data2 = f2.read()
        
        print("Its time")
        print("Data ready")
        (discard, sep, reading) = data.partition(' t=')
        t = float(reading) / 1000.0
        print("Sensor 1 {:.1f}".format(t))
        with open("Sensor1.txt", "a") as f:
            f.write("\n")
            now = datetime.now()
            current_minute = now.strftime("%H:%M")
            f.write(current_minute + " ," + str(t))
        
        print("Data 2 ready")
        (discard, sep, reading) = data2.partition(' t=')
        t = float(reading) / 1000.0
        print("Sensor 2 {:.1f}".format(t))
        with open("Sensor2.txt", 'a') as f:
            f.write("\n")
            now = datetime.now()
            current_minute = now.strftime("%H:%M")
            f.write(current_minute + " ," + str(t))

    else:
        time.sleep(20)
