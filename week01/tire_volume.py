# Title: W01 Project: Tire Volume
# Author: Nicholas Nixon
# Class: CSE 111
# Instructor: Thomas Reid
# Date: October 2025

import math
from datetime import datetime

tire_width = 0.0
tire_ratio = 0.0
tire_diameter = 0.0
tire_volume = 0.0
current_date = datetime.now()


tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = (tire_width * tire_ratio + 2540 * tire_diameter) * (math.pi * tire_width ** 2 * tire_ratio) / 10000000000

# write the following to tire_file date, width, ratio, diameter, volume
with open("volumes.txt", "at") as tire_file:
    print(f"{current_date:%Y-%m-%d}, {tire_width}, {tire_ratio}, {tire_diameter}, {tire_volume:.2f}", file=tire_file)

print(f"The approximate volume is {tire_volume:.2f} liters")