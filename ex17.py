#!/usr/bin/env python3
"""Learn Python the Hard Way - Exercise 17"""

from sys import argv

open(argv[2], 'w').write(open(argv[1]).read())
