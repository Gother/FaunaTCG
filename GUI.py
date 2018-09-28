import Board
import sys, termios, tty, os, time
import fcntl
import turtle
from time import sleep

# Register shapes
turtle.register_shape("graphics/blue.gif")
turtle.register_shape("graphics/dark_blue.gif")
turtle.register_shape("graphics/darker_blue.gif")
turtle.register_shape("graphics/red.gif")
turtle.register_shape("graphics/dark_red.gif")
turtle.register_shape("graphics/darker_red.gif")
turtle.register_shape("graphics/grey.gif")
turtle.register_shape("graphics/yellow.gif")

turtle.register_shape("graphics/animal/wolf.gif")
turtle.register_shape("graphics/animal/seal.gif")
turtle.register_shape("graphics/animal/penguin.gif")
turtle.register_shape("graphics/animal/panda.gif")
turtle.register_shape("graphics/animal/rabbit.gif")

def on_click(tile):
    tile.shape("graphics/yellow.gif")
    turtle.clear()

def initializeScreen():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.tracer(3)
    wn.screensize(400,400)
    wn.colormode(255)
    wn.title("Fauna TCBG")

def createAnimalBoard(animals):

    g_animals = []
    STARTPOINT = (-350, -150)
    for index in range(len(animals)):
        g_animal = turtle.Turtle()
        g_animal.speed(0)

        # Define colors and shape
        g_animal.shape("graphics/animal/" + animals[index].display)
        g_animal.penup()
        #g_animal.color(board.tiles[board.tilemap[row][column]])

        # Define positions on the screen
        posX = STARTPOINT[0]
        posY = STARTPOINT[1] + index * 100 + 2
        g_animal.setposition(posY, posX)

        g_animals.append(g_animal)
    turtle.pu()
    turtle.hideturtle()


def createGraphicalBoard(board):
    # Create graphical tiles
    g_tiles = []
    STARTPOINT = (-250,-150)
    turtle.colormode(255)
    for row in range (board.MAPHEIGHT):
        for column in range(board.MAPWIDTH):

            # Initialize turtle
            tile = turtle.Turtle()
            tile.speed(0)

            # Define colors and shape
            tile.shape(board.tiles[board.tilemap[row][column]])
            tile.penup()
            #tile.color(board.tiles[board.tilemap[row][column]])

            # Define positions on the screen
            posX = STARTPOINT[0] +  column * board.TILESIZE + 2
            posY = STARTPOINT[1] + row * board.TILESIZE + 2
            tile.setposition(posY, posX)

            # Functions over clicking
            tile.onclick(lambda x, y, t=tile: on_click(t))

            g_tiles.append(tile)
    turtle.pu()
    turtle.hideturtle()

    return g_tiles

def printBoard(board):
    turtle.hideturtle()
    g_tiles = createGraphicalBoard(board)
    for tile in g_tiles:
        print(tile.xcor(), tile.ycor(), tile.shape())
