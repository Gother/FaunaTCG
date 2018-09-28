import Card
import Board
import GUI
from curtsies import Input
import sys, termios, tty, os, time
import turtle
import os


def runGame():
    GUI.initializeScreen()
    board = Board.Tile()
    GUI.printBoard(board)
    animals = Card.loadAnimals()
    GUI.createAnimalBoard(animals)
    turtle.listen()
    turtle.mainloop()

if __name__ == "__main__":

    runGame()
