from graphics import *

win = Window(800, 600)
point1 = Point(40, 20)
point2 = Point(50, 80)
point3 = Point(10, 90)
point4 = Point(20, 60)
# line1 = Line(point1, point2)
# line2 = Line(point3, point4)
cell1 = Cell(win, point1, point2)
cell2 = Cell(win, point3, point4)
cell1.draw()
cell2.draw()
# win.draw_line(line1, "black")
# win.draw_line(line2, "black")
win.wait_for_close()