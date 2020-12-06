#!/bin/python3

import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

try:
    while True:
        print('Enter number:')

        try:
            user_input = int(input())
        except ValueError:
            print('Not a number')
            continue

        while user_input != 1:
            result = collatz(user_input)
            print(result)
            user_input = result
except KeyboardInterrupt:
    sys.exit()
