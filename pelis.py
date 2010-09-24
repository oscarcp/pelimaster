# -*- coding: utf-8 -*-

import sys
import random

f = open('lista.txt', 'r')
t = []

[t.append([line]) for line in f]

def generate_random():
    print '\n    %s' % (random.choice(t)[0])

while True:
    q = raw_input('* ¿Generar película? (s/n) ')
    [sys.exit(0) if q == 'n' or q == 'no' else generate_random()]