from src.graphics import *
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells(num_rows, num_cols)

    def _create_cells(self, rows, cols):
        tracker = []
        for i in range(rows):
            for j in range(cols):
                tracker.append(Cell(self.win))
            self._cells.append(tracker)
            tracker = []
        self._draw_cell()

    def _draw_cell(self):
        x = self.x1
        y = self.y1
        for column in self._cells:
            point1 = Point(x, y)
            point2 = Point(x + self.cell_size_x, y + self.cell_size_y)
            for cell in column:
                cell.draw(point1, point2)
                self._animate()
                y += self.cell_size_y
            x += self.cell_size_x
            y = self.y1


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)