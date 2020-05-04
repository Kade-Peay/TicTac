#!/bin/env python3
import random

def boardinit():
    board = [['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']]
    return board

def printBoard():
    for row in board:
        print(row)


def playerTurn():
    print("Numbers must be between 0 and 2")
    x = input("Enter 'X' Coordinate: ")
    y = input("Enter 'Y' Coodrinate: ")

    if int(x) > 2 or int(y) > 2:
        print("Invalid, try again")
        playerTurn()
    else:
        board[int(x)][int(y)] = 'X'

def compTurn():
    x = random.randint(0,2)
    y = random.randint(0, 2)

    if board[int(x)][int(y)] != 'X':
        board[int(x)][int(y)] = 'Y' 
    else: compTurn()

def check():

    # Horizontal Check of 'X'
    #----------------------------------------------------------------------------------
    if board[0][0] and board[0][1] and board[0][2] == 'X':
        print('X wins')
        gameGoing = False
    elif board[1][0] and board[1][1] and board[1][2] == 'X':
        print('X wins')
        gameGoing = False
    elif board[2][0] and board[2][1] and board[2][2] == 'X':
        print('X wins')
        gameGoing = False
    #----------------------------------------------------------------------------------

    # Vertical check of 'X'
    #----------------------------------------------------------------------------------
    elif board[0][0] and board[1][0] and board[2][0] == 'X':
        print('X wins')
        gameGoing = False
    elif board[0][1] and board[1][1] and board[2][1] == 'X':
        print('X wins')
        gameGoing = False
    elif board[0][2] and board[1][2] and board[2][2] == 'X':
        print('X wins')
        gameGoing = False
    #----------------------------------------------------------------------------------    

    # Horizontal Check of 'Y'
    #----------------------------------------------------------------------------------
    elif board[0][0] and board[0][1] and board[0][2] == 'Y':
        print('X wins')
        gameGoing = False
    elif board[1][0] and board[1][1] and board[1][2] == 'Y':
        print('X wins')
        gameGoing = False
    elif board[2][0] and board[2][1] and board[2][2] == 'Y':
        print('X wins')
        gameGoing = False
    #----------------------------------------------------------------------------------

    # Vertical check of 'Y'
    #----------------------------------------------------------------------------------
    elif board[0][0] and board[1][0] and board[2][0] == 'Y':
        print('X wins')
        gameGoing = False
    elif board[0][1] and board[1][1] and board[2][1] == 'Y':
        print('X wins')
        gameGoing = False
    elif board[0][2] and board[1][2] and board[2][2] == 'Y':
        print('X wins')
        gameGoing = False
    #----------------------------------------------------------------------------------    

# I am going to use this to loop over the game
def game():
    printBoard()
    print()
    playerTurn()
    check()
    if not gameGoing: exit()
    printBoard()
    print()
    compTurn()
    check()
    if not gameGoing: exit()
    printBoard()
    print()
    if not gameGoing: exit()


if __name__ == "__main__":
    board = boardinit()
    gameGoing = True
    game()