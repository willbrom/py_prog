#!/usr/bin/python3

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase]')
    sys.exit()

keyphrase = sys.argv[1]
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for %s copied to clipboard' % keyphrase)
    sys.exit()

print('argument not present. (agree, busy, upsell)')
