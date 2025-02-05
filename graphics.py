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
        left_line = Line(Point(point1.x, point1.y), Point(point1.x, point2.y))
        right_line = Line(Point(point2.x, point1.y), Point(point2.x, point2.y))
        top_line = Line(Point(point1.x, point1.y), Point(point2.x, point1.y))
        bottom_line = Line(Point(point1.x, point2.y), Point(point2.x, point2.y))
        self._box_map = [
            [left, right, top, bottom], 
            [left_line, right_line, top_line, bottom_line]
        ]
        self.point1 = point1
        self.point2 = point2
        self._win = window

    def draw(self):
        count = 0
        for wall in self._box_map[0]:
            if wall:
                self._win.draw_line(self._box_map[1][count])
            count += 1