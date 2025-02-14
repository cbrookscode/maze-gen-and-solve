from tkinter import *

class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Root Widget Title Placeholder")
        self.__canvas = Canvas(self.__root, background="white")
        self.__canvas.pack(fill="both", expand=True)
        self.__isrunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.__root.destroy)
        self.width = width
        self.height = height


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isrunning = True
        while self.__isrunning:
            self.redraw()

    def close(self):
        self.__isrunning = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    


class Line:

    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2
        
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)


class Cell:

    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.walls = [self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall]
        self._win = window
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.visited = False

    # draw cell
    def draw(self, point1, point2):
        left_line = Line(Point(point1.x, point1.y), Point(point1.x, point2.y))
        right_line = Line(Point(point2.x, point1.y), Point(point2.x, point2.y))
        top_line = Line(Point(point1.x, point1.y), Point(point2.x, point1.y))
        bottom_line = Line(Point(point1.x, point2.y), Point(point2.x, point2.y))

        lines = [(left_line, self.has_left_wall), (right_line, self.has_right_wall), (top_line, self.has_top_wall), (bottom_line, self.has_bottom_wall)]

        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

        for line, has_wall in lines:
            if has_wall:
                self._win.draw_line(line)
            else:
                self._win.draw_line(line, fill_color="white")


    # draw line between center point of two cells
    def draw_move(self, to_cell, undo=False):
        cell1_center_x = (self.x1 + self.x2) / 2
        cell2_center_x = (to_cell.x1 + to_cell.x2) / 2
        cell1_center_y = (self.y1 + self.y2) / 2
        cell2_center_y = (to_cell.y1 + to_cell.y2) / 2
        
        centering_line = Line(Point(cell1_center_x, cell1_center_y), Point(cell2_center_x, cell2_center_y))
        if undo:
            self._win.draw_line(centering_line, "white")
        else:
            self._win.draw_line(centering_line, "red")


    def is_same_cell(self, other):
        if self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2:
            return True
        else:
            return False