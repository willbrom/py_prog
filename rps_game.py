#!/bin/python3

import random
import sys

win, loss, tie = 0, 0, 0

print('ROCK, PAPER, SCISSORS')

while True:
	print(str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties' )
	print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

	# conditions within conditions
	move = input();
	rand_move = random.randint(1,3)
	
	if rand_move == 1:
		rand_move = 'r'
	elif rand_move == 2:
		rand_move = 'p'
	elif rand_move == 3:
		rand_move = 's'

	if move ==  'q':
		sys.exit()
	elif move == 'r':
		print('ROCK versus...')
		if rand_move == 'r':
			print('ROCK')
			print('It is a tie!')
			tie = tie + 1
		elif rand_move == 'p':
			print('PAPER')
			print('You loss!')
			loss = loss + 1
		elif rand_move == 's':
			print('SCISSORS')
			print('You win!')
			win = win + 1
	elif move == 'p':
		print('PAPER versus...')
		if rand_move == 'r':
			print('ROCK')
			print('You win!')
			win = win + 1
		elif rand_move == 'p':
			print('PAPER')
			print('It is a tie!')
			tie = tie + 1
		elif rand_move == 's':
			print('SCISSORS')
			print('You loss!')
			loss = loss + 1
	elif move == 's':
		print('SCISSORS versus...')
		if rand_move == 'r':
			print('ROCK')
			print('You loss!')
			loss = loss + 1
		elif rand_move == 'p':
			print('PAPER')
			print('You win!')
			win = win + 1
		elif rand_move == 's':
			print('SCISSORS')
			print('It is a tie!')
			tie = tie + 1
	else:
		print('No such command!')
