from src.graphics import *
from src.maze import *

win = Window(5000, 5000)

mytestmaze = Maze(15, 15, 12, 15, 50, 50, win)
mytestmaze.solve()


win.wait_for_close()