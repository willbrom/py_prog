#!/bin/python3

import sys, time

count = 4
dec = True

def print_stars(count):
    print(' ' * count + '********')

try:
    while True:
        print_stars(count)
        time.sleep(0.1)
        if dec:
            count = count - 1
            if count == 0:
                dec = False
        else:
            count = count + 1
            if count == 4:
                dec = True
except KeyboardInterrupt:
    sys.exit()
