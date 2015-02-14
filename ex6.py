#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 6"""

# Assign simple and formatted strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the formatted strings
print(x)
print(y)

# Print formatted strings containing formatted strings
print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# More string formatting
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

# Simple string concatenation
print(w + e)
