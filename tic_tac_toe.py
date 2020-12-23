#!/bin/python3

import pprint

board = {'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': '', 'mid-M': '', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': ''}
moves = 'top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R' 
win_conditions = [['top-L', 'top-M', 'top-R'], ['mid-L', 'mid-M', 'mid-R'], ['low-L', 'low-M', 'low-R']]
player = 'P1'
victory = False

print()
print('*********************************************************')
print('available moves: %s'% moves)
print('*********************************************************')
print()

while not victory:
    pprint.pprint(board)
    
    move = input('%s, Enter move: '% player)

    if move not in board.keys():
        print('Unknown move')
        continue

    if board[move] != '':
        print('Not allowed(contain "%s")'% board[move])
        continue

    if player == 'P1':
        board[move] = 'X'
        player = 'P2'
    else:
        board[move] = 'O'
        player = 'P1'

    for condition in win_conditions:
        count = 0
        for square in condition:
            if (player == 'P1' and board[move] == 'X') or (player == 'P2' and board[move] == 'O'):
                count += 1
        if count == 3:
            victory = True
            print('Victory for %s'% player)
            break

