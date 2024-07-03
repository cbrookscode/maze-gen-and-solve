from graphics import *
from cell import *
import time

class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        ):

        self.xcord = x1
        self.ycord = y1
        self.rows = num_rows
        self.columns = num_cols
        self.cellsizex = cell_size_x
        self.cellsizey = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for i in range(self.columns):
            listofcells = []
            for j in range(self.rows):
                x1 = self.xcord + (i * self.cellsizex)
                y1 = self.ycord + (j * self.cellsizey) 
                x2 = x1 + self.cellsizex
                y2 = y1 + self.cellsizey
                listofcells.append(Cell(Point(x1, y1), Point(x2, y2), self.win))
            self._cells.append(listofcells)


    def _draw_cell(self):
        if self.win is None:
            return
        for columns_of_cells in self._cells:
            for cell in columns_of_cells:
                cell.draw_cell()
                self._animate()


    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)
