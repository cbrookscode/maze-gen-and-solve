from tkinter import *

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.title = self.root.title("My Tkinter Window")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.grid()
        self.isrunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.isrunning = True
        while self.isrunning == True:
            self.redraw()

    def close(self):
        self.isrunning = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )