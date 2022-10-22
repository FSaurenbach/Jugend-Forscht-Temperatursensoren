#!/usr/bin/env python
from datetime import datetime  # Zeit modul um festzulegen wie oft messungen gemacht werden
import time


def is_time():
    now = datetime.now()
    current_minute = now.strftime("%M")
    if current_minute == "30" or current_minute == "00":
        return True
    else:
        return False


sensor1 = "/sys/bus/w1/devices/28-3c01f0960400/w1_slave"  # Sensor 1
sensor2 = "/sys/bus/w1/devices/28-3c01f096db57/w1_slave"  # Sensor 2
f = open(sensor1, "r")  # Auf beide Sensoren zugreifen
f2 = open(sensor2, "r")

sensor1_text = open("Sensor1.txt", "w")
sensor2_text = open("Sensor2.txt", "w")

data = f.read()  # Die Daten auslesen
data2 = f2.read()
f.close()
f2.close()

while True:
    if is_time():
        if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 10.0
            print("Sensor 1 {:.1f}".format(t))
            with open("Sensor1.txt", "a") as f:
                f.write('\n'.join(str(t)))
        if "YES" in data2:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 10.0
            print("Sensor 2 {:.1f}".format(t))
            with open("Sensor2.txt", 'a') as f:
                f.write('\n'.join(str(t)))
        else:
            print("ERROR")
        time.sleep(120)
    else:
        time.sleep(20)
