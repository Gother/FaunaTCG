
class Tile:
    TILESIZE = 100
    MAPWIDTH = 5
    MAPHEIGHT = 5

    BASE_BLUE = 0
    BASE_RED = 1
    SPAWN_BLUE = 2
    SPAWN_RED = 3
    EMPTY = 4
    FIELD_BLUE = 5
    FIELD_RED = 6
    MIDDLE = 7

    BLUE = "graphics/blue.gif" #(51, 153, 255)
    DARK_BLUE = "graphics/dark_blue.gif" #(0, 102, 255)
    DARKER_BLUE = "graphics/darker_blue.gif" #(0, 51, 204)

    RED = "graphics/red.gif" #(255, 80, 80)
    DARK_RED = "graphics/dark_red.gif" #(204, 0, 0)
    DARKER_RED = "graphics/darker_red.gif" #(153, 0, 0)

    GREY = "graphics/grey.gif" #(191, 191, 191)
    YELLOW = "graphics/yellow.gif" #(205, 205, 0)

    tiles = {
        BASE_BLUE : DARK_BLUE,
        BASE_RED : DARK_RED,
        SPAWN_BLUE : DARKER_BLUE,
        SPAWN_RED : DARKER_RED,
        EMPTY : GREY,
        FIELD_BLUE : BLUE,
        FIELD_RED : RED,
        MIDDLE: YELLOW
    }

    tilemap = [
        [BASE_RED, EMPTY, EMPTY, EMPTY, SPAWN_RED],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, MIDDLE, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [SPAWN_BLUE, EMPTY, EMPTY, EMPTY, BASE_BLUE]
    ]

    tilemap4 = [
        [BASE_RED, EMPTY, EMPTY, SPAWN_RED],
        [EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY],
        [SPAWN_BLUE, EMPTY, EMPTY, BASE_BLUE]
    ]
