#!/usr/bin/python3

import sys, pyperclip

phrase = pyperclip.paste()

if not phrase:
    print('clipboard empty')
    sys.exit()

splitted_phrase = phrase.split("\n")
new_phrase = ''
for phrase in splitted_phrase:
    new_phrase += f'* {phrase}\n'
pyperclip.copy(new_phrase[:-1])

print('clipboard updated')
