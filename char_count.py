#!/bin/python3

import sys

try:
    user_input = sys.argv[1]
except IndexError:
    print('No user input provided\nExiting now')
    sys.exit()

result = {}
for text in user_input:
    result.setdefault(text, 0)
    result[text] = result[text] + 1
    
print(result)
