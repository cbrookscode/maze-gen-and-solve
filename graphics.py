from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Root Widget Title Placeholder")
        self.__canvas = Canvas(self.__root, background="white")
        self.__canvas.pack()
        self.__isrunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


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

    def __init__(self, window, point1, point2, left=True, right=True, top=True, bottom=True):
        self._has_left_wall = left
        self._has_right_wall = right
        self._has_top_wall = top
        self._has_bottom_wall = bottom
        self._x1 = point1.x
        self._x2 = point1.y
        self._y1 = point2.x
        self._y2 = point2.y
        self._win = window

    def draw(self):
        if self._has_left_wall:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_line)
        if self._has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line)
        if self._has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line)
        if self._has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line)