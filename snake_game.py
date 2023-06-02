# This is a simple snake game with the snake eating the food
# @author: Anirudh Asuri Mukundan
# @begin date: 1st June 2023

# Game objective: snake eating the food
# Game rules:
# 1. Hitting the corner ends the game
# 2. Eating the food increases snake's length
# 3. Crashing onto itself ends the game

import numpy as np
import matplotlib.pyplot as plt
import random
import curses # used to initialize the screen

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx() # get the screen height and width
w = curses.newwin(sh, sw, 0, 0) # create a new window with the specified height and width and the origin placed at top left corner of the screen (0, 0)
w.keypad(1) # setting the program to accept keypad input
w.timeout(100) # refresh the screen every 100 milliseconds

# creating snake's initial position
snake_x = int(sw/4)
snake_y = int(sh/2)

# creating snake's body as 3 blocks of screen pixel
snake = [ [snake_y, snake_x], [snake_y, snake_x-1], [snake_y, snake_x-2] ]

# create the food
food = [int(sh/2), int(sw/2)] # food located at center of the screen
w.addch(food[0], food[1], curses.ACS_PI) # add the food to the screen using add character function

# initial direction of motion of snake
key = curses.KEY_RIGHT

# Track the movement of the snake
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # end of the game "condition"
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # determine location of new head of the snake based on user key input
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1

    # insert new head of the snake
    snake.insert(0, new_head)

    # determine if snake has eaten the food
    if snake[0] == food:
        food = None # remove the current location of food
        while food is None: # add new food location randomnly
            nf = [ 
                random.randint(1, sh-1), 
                random.randint(1, sw-1) 
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI) # add the food at its new location
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ') # add a space character where the tail originally was

    # add head of the snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
