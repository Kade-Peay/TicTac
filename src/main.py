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

# Make this a choice between 1 and 9
def playerTurn():
    print("Choose Number between 1 and 9")
    choice = input("Enter number: ")

    if choice == '1':
        x = 0
        y = 0
    elif choice == '2':
        x = 0
        y = 1
    elif choice == '3':
        x = 0
        y = 2
    elif choice == '4':
        x = 1
        y = 0
    elif choice == '5':
        x = 1
        y = 1
    elif choice == '6':
        x = 1
        y = 2
    elif choice == '7':
        x = 2
        y = 0
    elif choice == '8':
        x = 2
        y = 1
    elif choice == '9':
        x = 2
        y = 2
    else:
        print('Invalid input')

    if board[x][y] != '-':
        print("That spot is taken")
        playerTurn()
    else:
        board[x][y] = 'X'

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
    ex = [['1', '2', '3'],
    ['4', '5', '6'],
    ['7','8','9']]
    for row in ex:
        print(row)
    print()
    printBoard()
    game()