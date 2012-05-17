#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

A = input(u'a: ')
B = input(u'b: ')
C = input(u'c: ')

def solve():
    """
    - As bugs reproduce?
    - Well, the programmers with them at night fuck.
    """
    try :
        DD = B*B - 4.0*A*C
        if DD >= 0.0:
            x1 = (-B + math.sqrt(DD)) / (2.0 * A)
            x2 = (-B - math.sqrt(DD)) / (2.0 * A)

            return [x1, x2]
        else:
            return []
    except TypeError:
        print u'Transferred to incorrect values'

R = solve()
print(R)