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
    pass

# I am going to use this to loop over the game
def game():
    printBoard()
    playerTurn()
    # check()
    printBoard()
    # compTurn()
    # check()
    # printBoard()
    # game()


if __name__ == "__main__":
    board = boardinit()
    game()