#CSCI 1133, Lab Section 013, HW 1 ANDY_COLUMBUS, Problem 1A
# so can I type whatever I want here? because it doesn't impact my grades and code?
import math
incidentAngle = float (input("Input incident angle in degrees: "))
incidentAngle = math.radians(incidentAngle)
n1 = float (input("Input index of refraction of first medium: "))
n2 = float (input("Input index of refraction of second medium: "))
angleOfRefraction = math.asin(math.sin(incidentAngle) * n1/n2)
print("Angle of Refraction: ", math.degrees(angleOfRefraction), " degrees ")

# CSCI 1133, Lab Section 013, HW 1 ANDY_COLUMBUS, Problem 1B
# wow I hate programming

import math

print ("This program converts fahrenheit temperatures to celsius and kelvin")

temp = float (input(" Please enter the temperature in Fahrenheit "))
# remeber is F to C not C to F
celsius = (temp - 32 ) * (5/9)
kelvin = (temp - 32) * (5/9) + 273.15

print ("The temperature in Celsius is: " , celsius )
print ("The temperature in Kelvin is: " , kelvin)

if temp > 70:
    print (" OWO is hot outside")

if temp < 50:
    print ( "It is cold!")

if  70 <= temp >= 50:
    print (" just another day in Minnesota")

# not gonna lie tho I rather do this than a libe eassy