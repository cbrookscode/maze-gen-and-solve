from src.graphics import *
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if num_rows == 0 or num_cols == 0:
            raise Exception("Maze cannot have 0 rows or columns when created")
        if num_rows < 0 or num_cols < 0:
            raise Exception("Maze cannot a negative value for either rows or columns when created")
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None
        self.seed = None
        if seed is not None:
            self.seed = random.seed(seed)

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
    
    def is_valid_cell(self, i_j_tuple):
        return (i_j_tuple[0] >= 0 and 
                i_j_tuple[0] < len(self._cells) and 
                i_j_tuple[1] >= 0 and 
                i_j_tuple[1] < len(self._cells[0]))
    
    def _break_walls_r(self, i , j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            not_visited =[]
            left = (i - 1, j)
            right = (i + 1 , j)
            top = (i, j - 1)
            bottom = (i, j + 1)
            if self.is_valid_cell(left) == True and self._cells[left[0]][left[1]].visited == False:
                not_visited.append(left)

            if self.is_valid_cell(right) == True and self._cells[right[0]][right[1]].visited == False:
                not_visited.append(right)

            if self.is_valid_cell(top) == True and self._cells[top[0]][top[1]].visited == False:
                not_visited.append(top)

            if self.is_valid_cell(bottom) == True and self._cells[bottom[0]][bottom[1]].visited == False:
                not_visited.append(bottom)

            if len(not_visited) == 0:
                current_cell.draw(Point(current_cell.x1, current_cell.y1), Point(current_cell.x2, current_cell.y2))
                self._animate()
                return
            else:
                random_index = None
                if self.seed != None:
                    random_index = self.seed
                else:
                    random_index = random.randrange(0, len(not_visited))
                new_i = not_visited[random_index][0]
                new_j = not_visited[random_index][1]
                if new_i == i and new_j == j + 1:
                    current_cell.has_bottom_wall = False
                    self._break_walls_r(new_i, new_j)
                if new_i == i and new_j == j - 1:
                    current_cell.has_top_wall = False
                    self._break_walls_r(new_i, new_j)
                if new_i == i + 1 and new_j == j:
                    current_cell.has_right_wall = False
                    self._break_walls_r(new_i, new_j)
                if new_i == i - 1 and new_j == j:
                    current_cell.has_left_wall = False
                    self._break_walls_r(new_i, new_j)