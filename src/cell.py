from graphics import Point, Line, Window

class Cell:
    def __init__(self, point1, point2, window, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        self._win = window
    
    def draw_cell(self):
        if self.has_left_wall == True:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(self._win.canvas, "red")
        if self.has_top_wall == True:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(self._win.canvas, "red")
        if self.has_right_wall == True:
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(self._win.canvas, "red")
        if self.has_bottom_wall == True:
            Line(Point(self._x2, self._y2), Point(self._x1, self._y2)).draw(self._win.canvas, "red")
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo == True:
            color = "gray"
        point1 = Point(((self._x2 + self._x1) / 2), ((self._y2 + self._y1) / 2))
        point2 = Point(((to_cell._x2 + to_cell._x1) / 2), ((to_cell._y2 + to_cell._y1) / 2))
        Line(point1, point2).draw(self._win.canvas, color)
