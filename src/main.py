
from cell import Cell
from graphics import Window, Point
def main():
    win = Window(800, 600)
    cell1 = Cell(Point(200, 200), Point(500, 500), win, bottom_wall=False)
    cell2 = Cell(Point(250, 250), Point(550, 550), win)
    cell3 = Cell(Point(300, 300), Point(500, 500), win, top_wall=False)
    cell4 = Cell(Point(350, 350), Point(500, 500), win, right_wall=False)

    cell3.draw_cell()

    win.wait_for_close()




main()