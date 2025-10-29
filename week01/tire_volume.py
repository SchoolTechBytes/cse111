# Title: W01 Project: Tire Volume
# Author: Nicholas Nixon
# Class: CSE 111
# Instructor: Thomas Reid
# Date: October 2025


    # Have the user enter a tire width in mm.
    # Have the user enter the aspect ratio.
    # Have the user enter the diameter of the wheel in inches.
    # Calculate and display the tire's volume.
    # Log the information in a text file.
    #     current date (Do NOT include time)
    #     width of the tire
    #     aspect ratio of the tire
    #     diameter of the wheel
    #     volume of the tire (rounded to two decimal places)


# Milestone

# Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.
#     Create a folder for this week's project, name it whatever you want.
#     Open the folder you just created in VSCode.
#     Create a file named tire_volume.py.
#     Write the program to ask the user for the 3 items in the requirements and output the tire volume.

import math

tire_width = 0.0
tire_ratio = 0.0
tire_diameter = 0.0
tire_volume = 0.0


tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = (tire_width * tire_ratio + 2540 * tire_diameter) * (math.pi * tire_width ** 2 * tire_ratio) / 10000000000

print(f"The approximate volume is {tire_volume:.2f} liters")