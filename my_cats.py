#!/bin/python3

import random

cats = []
while True:
    cat = input('Enter name of cat %s, or empty value to proceed: '% str(len(cats) + 1))
    if cat == '':
        break
    cats = cats + [cat]

random.shuffle(cats)
print('*' * 40, 'These are the names of your cats:', sep='\n')
for i, cat in enumerate(cats):
    print('  ' + str(i + 1) + '. ' + cat)
