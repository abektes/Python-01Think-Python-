# -*- coding: utf-8 -*-

from __future__ import division
import math


signal_power = 9
noise_power = 10
ratio  = signal_power / noise_power

decibels = 10 * math.log10(ratio)

print decibels


# Fermat's Last Theorem  a,  and c


def check_fermat(a, b, c, n):

    if n > 2 and (a**n + b**n == c**n):
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesn’t work.'

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a, b, c, n)


def is_triangle(a1,a2,a3):
    if abs(a1 - a2) < abs(a3) and abs(a1 + a2 ) > abs(a3):
        print "It is a triangle"
    else:
        print "It is not a triangle"

def check_numbers2():
    a1 = int(input("Choose a number for a1: "))
    a2= int(input("Choose a number for a2: "))
    a3 = int(input("Choose a number for a3: "))
    return is_triangle(a1,a2,a3)

check_numbers2()