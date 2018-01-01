#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 14"""

from sys import argv

script, first_name, last_name = argv
prompt = '\u279F '

print("Hi, %s %s, I'm the %s script." % (first_name, last_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me, %s?" % first_name)
likes = input(prompt)

print("Where do you live, %s?" % first_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
