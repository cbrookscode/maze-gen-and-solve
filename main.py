from src.graphics import *
from src.maze import *

win = Window(800, 600)

mytestmaze = Maze(15, 15, 3, 3, 50, 50, win)

win.wait_for_close()