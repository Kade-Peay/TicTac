#!/bin/env python3
import random, sys

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
    elif board[int(x)][int(y)] == 'y':
        print("That spot is taken")
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
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    #----------------------------------------------------------------------------------

    # Vertical check of 'X'
    #----------------------------------------------------------------------------------
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    #----------------------------------------------------------------------------------    

    # Diagonal check of 'X'
    #---------------------------------------------------------------------------------- 
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        print('X wins')
        printBoard()
        sys.exit()
    #---------------------------------------------------------------------------------- 

    # Diagonal check of 'Y'
    #---------------------------------------------------------------------------------- 
    elif board[0][0] == 'Y' and board[1][1] == 'Y' and board[2][2] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    elif board[2][0] == 'Y' and board[1][1] == 'Y' and board[0][2] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    #---------------------------------------------------------------------------------- 

    # Horizontal Check of 'Y'
    #----------------------------------------------------------------------------------
    elif board[0][0] == 'Y' and board[0][1] == 'Y' and board[0][2] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    elif board[1][0] == 'Y' and board[1][1] == 'Y' and board[1][2] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    elif board[2][0] == 'Y' and board[2][1] == 'Y' and board[2][2] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    #----------------------------------------------------------------------------------

    # Vertical check of 'Y'
    #----------------------------------------------------------------------------------
    elif board[0][0] == 'Y' and board[1][0] == 'Y' and board[2][0] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    elif board[0][1] == 'Y' and board[1][1] == 'Y' and board[2][1] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    elif board[0][2] == 'Y' and board[1][2] == 'Y' and board[2][2] == 'Y':
        print('Y wins')
        printBoard()
        sys.exit()
    #----------------------------------------------------------------------------------    

# I am going to use this to loop over the game
def game():
    printBoard()
    print()
    print("Your Turn!")
    playerTurn()
    check()
    print("Computer's Turn!")
    compTurn()
    check()
    printBoard()
    print()
    game()


if __name__ == "__main__":
    board = boardinit()
    game()