#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 20"""

from sys import argv

script, input_file = argv

# Print contents of the file
def print_all(f):
    print(f.read())

# Move file read pointer to the beginning of the file
def rewind(f):
    f.seek(0)

# Print line_count and the next line in the file
# Note that line_count is arbitrary and does not affect the read pointer
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # 2
print_a_line(current_line, current_file)

current_line += 1 # 3
print_a_line(current_line, current_file)
