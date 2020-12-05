#!/bin/python3

#This is a guess the number game

from random import randint

rand_num = randint(1,20)

print('I am thinking of a number between 1 and 20')

for guess_taken in range(0, 7):
	print('Take a guess')
	guess = int(input())
	if guess < rand_num:
		print('Your guess is too low')
	elif guess > rand_num:
		print('Your guess is too high')
	else:
		break

if guess == rand_num:
	print('Good job! you guessed my number in ' + str(guess_taken + 1) + ' guesses!')
else:
	print('Better luck next time, scrub!')
