#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

A = input(u'a: ')
B = input(u'b: ')
C = input(u'c: ')

D = B*B - 4.0*A*C

x1 = (-B + math.sqrt(D)) / (2.0 * A)
x2 = (-B - math.sqrt(D)) / (2.0 * A)

print x1, x2