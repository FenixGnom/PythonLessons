#!/usr/bin/python
# -*- coding: utf-8 -*-

import equation


A = input(u'a: ')
B = input(u'b: ')
C = input(u'c: ')

R = equation.solve(A,B,C)
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