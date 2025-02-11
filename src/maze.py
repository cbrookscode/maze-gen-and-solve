from src.graphics import *
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if num_rows == 0 or num_cols == 0:
            raise Exception("Maze cannot have 0 rows or columns when created")
        if num_rows < 0 or num_cols < 0:
            raise Exception("Maze cannot a negative value for either rows or columns when created")
        if seed is not None:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None

        self._create_cells(num_rows, num_cols)

    def _create_cells(self, rows, cols):
        self._cells = [[Cell(self.win) for row in range(rows)] for cols in range(cols)]
        self._draw_cell()

    def _draw_cell(self):
        if self.win == None:
            raise Exception("window is None")
        x = self.x1
        y = self.y1
        for column in self._cells:
            for cell in column:
                point1 = Point(x, y)
                point2 = Point(x + self.cell_size_x, y + self.cell_size_y)
                cell.draw(point1, point2)
                self._animate()
                y += self.cell_size_y
            x += self.cell_size_x
            y = self.y1
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        entrance.draw(Point(entrance.x1, entrance.y1), Point(entrance.x2, entrance.y2))
        self._animate()

        exit = self._cells[-1][-1]
        exit.has_bottom_wall = False
        exit.draw(Point(exit.x1, exit.y1), Point(exit.x2, exit.y2))
        self._animate()
    
    def is_valid_cell(self, i, j):
        return (i >= 0 and 
                i < len(self._cells) and 
                j >= 0 and 
                j < len(self._cells[0]))
    
    def _break_walls_r(self, i , j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            visited = []
            not_visited =[]
            # how to check adjacent cells? check all four sides. how to check a side. top and bottom easy as they are the before and after part of the list. left and right would be the same index but the before and after list.
            if self.is_valid_cell(i - 1, j) == True:
                if self._cells[i - 1][j].visited == False:
                    not_visited.append(self._cells[i - 1][j])
                else:
                    visited.append(self._cells[i - 1][j])

            if self.is_valid_cell(i + 1, j) == True:
                if self._cells[i + 1][j].visited == False:
                    not_visited.append(self._cells[i + 1][j])
                else:
                    visited.append(self._cells[i + 1][j])

            if self.is_valid_cell(i, j - 1) == True:
                if self._cells[i][j - 1].visited == False:
                    not_visited.append(self._cells[i][j - 1])
                else:
                    visited.append(self._cells[i][j - 1])

            if self.is_valid_cell(i, j + 1) == True:
                if self._cells[i][j + 1].visited == False:
                    not_visited.append(self._cells[i][j + 1])
                else:
                    visited.append(self._cells[i][j + 1])

            if len(visited) == 0:
                current_cell.draw(Point(current_cell.x1, current_cell.y1), Point(current_cell.x2, current_cell.y2))
                self._animate()
                return
            else:
                random_index = random.randrange(0, len(not_visited))
                new_cell = not_visited[random_index]
                new_cell.visited = True
                # with the x and y points for the new cell and old cell, how to determine which wall they share?
                if new_cell.x1 == current_cell.x1 and new_cell.x2 == current_cell.x2:
                    #share a top or bottom line
                    if Point(new_cell.x1, new_cell.y1) == Point(current_cell.x1, current_cell.y2):
                        #share a bottom wall
                        current_cell.has_bottom_wall = False
                        self._break_walls_r(i, j + 1)
                    else:
                        #share a top wall
                        current_cell.has_top_wall = False
                        self._break_walls_r(i, j - 1)
                if new_cell.y1 == current_cell.y1 and new_cell.y2 == current_cell.y2:
                    #share a left or right line
                    if Point(new_cell.x1, new_cell.y1) == Point(current_cell.x2, current_cell.y1):
                        #share a right wall
                        current_cell.has_right_wall = False
                        self._break_walls_r(i + 1, j)
                    else:
                        #share a left wall
                        current_cell.has_left_wall = False
                        self._break_walls_r(i - 1, j)