#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 5"""

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_to_cm = 2.54
lbs_to_kg = 0.45359237

print("Let's talk about %s." % name)
print("He's %d inches (or %.1f cm) tall." % (height, height * inch_to_cm))
print("He's %d pounds (or %.2f kg) heavy." % (weight, weight * lbs_to_kg))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight))
