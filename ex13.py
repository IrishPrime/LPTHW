#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 13"""

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
fourth = input("Give me one more value: ")
print("Your fourth variable is:", fourth)
