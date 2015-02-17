#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 19"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


def triple(arg):
    print(arg * 3)


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


foo = "foo"
formatter = "%s %s "
formatted = formatter % ("one", "two")

triple(4)
triple(6 * 4)
triple("String Literal")
triple(foo)
triple(foo + str(2))
triple(foo * 2)
triple(foo + "bar")
triple(formatter % ("first", "second"))
triple(formatted)
triple(foo + " " + formatted)
