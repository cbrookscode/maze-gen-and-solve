from cell import Cell
from graphics import Window, Point
from maze import *

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 10, 10, 5, 5, win)
    maze._draw_cell()

    win.wait_for_close()




main()