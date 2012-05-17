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