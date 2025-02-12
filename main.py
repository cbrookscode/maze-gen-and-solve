from src.graphics import *
from src.maze import *

win = Window(800, 600)

mytestmaze = Maze(15, 15, 3, 3, 50, 50, win, 2)

win.wait_for_close()