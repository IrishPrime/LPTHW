#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 3"""

# Python 3 converts to floats implicitly when needed, and additional
# calculations have been placed at the end of the file rather than in a new
# file (as requested in the exercise)

# A simple print statement
print("I will now count my chickens:")

# Print statements with strings and inline calculations
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# Arithmetic follows standard order of operations
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Ask a question
print("Is it true that 3 + 2 < 5 - 7?")

# Answer the question
print(3 + 2 < 5 - 7)

# Talk down to the user
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

# Taunt the user
print("How about some more.")

# Work out inequalities
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Exponents also work
print("What is 2^3?", 2 ** 3)
print("What is 2^4?", 2 ** 4)
print("What is 2^5?", 2 ** 5)
