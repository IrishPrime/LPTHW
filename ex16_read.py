#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 16 (Read)"""

from sys import argv

script, filename = argv

print("Opening the file: %s" % filename)
target = open(filename, 'r')

print("Read the contents...")
lines = target.read()

print("Print each line...\n")
print(lines)

print("And finally, we close it.")
target.close()
