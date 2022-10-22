#!/usr/bin/env python
import glob
import time # Zeit modul um festzulegen wie oft messungen gemacht werden
sensor1 = "/sys/bus/w1/devices/28-3c01f0960400/w1_slave" # Sensor 1
sensor2 = "/sys/bus/w1/devices/28-3c01f096db57/w1_slave" # Sensor 2
f = open(sensor1, "r") # Auf beide Sensoren zugreifen
f2 = open(sensor2, "r")
data = f.read() # Die Daten auslesen
data2 = f2.read()
f.close()
f2.close()
if "YES" in data:
   (discard, sep, reading) = data.partition(' t=')
   t = float(reading) / 1000.0
print("Sensor 1{} {:.1f}".format(id, t))
if "YES" in data2:
   (discard, sep, reading) = data.partition(' t=')
   t = float(reading) / 1000.0
   print("Sensor 2{} {:.1f}".format(id, t))
else:
  print("ERROR")



