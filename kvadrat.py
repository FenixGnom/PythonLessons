#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def solve(AA,BB,CC):
    try :
        DD = BB*BB - 4.0*AA*CC
        if DD >= 0.0:
            x1 = (-BB + math.sqrt(DD)) / (2.0 * AA)
            x2 = (-BB - math.sqrt(DD)) / (2.0 * AA)

            return [x1, x2]
        else:
            return []
    except TypeError:
        print u'Transferred to incorrect values'


A = input(u'a: ')
B = input(u'b: ')
C = input(u'c: ')

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