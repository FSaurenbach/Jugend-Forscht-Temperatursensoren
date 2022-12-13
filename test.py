#!/usr/bin/env python
from datetime import datetime  # Zeit modul um festzulegen wie oft messungen gemacht werden
import time
now = datetime.now()
current_minute = now.strftime("%M")
while True:
    print(current_minute)