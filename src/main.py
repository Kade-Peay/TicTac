#!/bin/env python3

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
    pass

def check():

    # Horizontal Check of 'X'
    #----------------------------------------------------------------------------------
    if board[0][0] and board[0][1] and board[0][2] == 'X':
        print('X wins')
    elif board[1][0] and board[1][1] and board[1][2] == 'X':
        print('X wins')
    elif board[2][0] and board[2][1] and board[2][2] == 'X':
        print('X wins')
    #----------------------------------------------------------------------------------

# I am going to use this to loop over the game
def game():
    printBoard()
    print()
    playerTurn()
    check()
    printBoard()
    print()
    # compTurn()
    # check()
    # printBoard()
    # print()
    game()


if __name__ == "__main__":
    board = boardinit()
    game()