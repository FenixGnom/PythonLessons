#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def solve(AA,BB,CC):
    if type(AA) == float and type(BB) == float and type(CC) == float :
        DD = BB*BB - 4.0*AA*CC
        if DD >= 0.0:
            x1 = (-BB + math.sqrt(DD)) / (2.0 * AA)
            x2 = (-BB - math.sqrt(DD)) / (2.0 * AA)

            return [x1, x2]
        else:
            return []
    else :
        return [u'Transferred to incorrect values']


A = float(input(u'a: '))
B = float(input(u'b: '))
C = float(input(u'c: '))

R = solve(A,B,C)
print(R)

#D = B*B - 4.0*A*C
#if D >= 0.0 :
#    x1 = (-B + math.sqrt(D)) / (2.0 * A)
#    x2 = (-B - math.sqrt(D)) / (2.0 * A)
#
#    print x1, x2
#
#else :
#    print u'No soution'
#
#print u'END'