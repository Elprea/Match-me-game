# boxview.py

from graphics import *


class BoxView:

    def __init__(self, win):
        self.win = win

        self.y1list = []
        y1 = 105
        self.y2list = []
        y2 = 230
        self.x1list = []
        self.x2list = []

        # box coordinates
        for col in range(4):
            x1 = 50
            x2 = 185
            for row in range(5):
                self.x1list.append(x1)
                self.x2list.append(x2)
                self.y1list.append(y1)
                self.y2list.append(y2)
                x1 = x2 + 20
                x2 = x1 + 135

            y1 = y2 + 20
            y2 = y1 + 125

        # plotting of boxes
        for i in range(20):
            rect = Rectangle(Point(self.x1list[i], self.y1list[i]), Point(self.x2list[i], self.y2list[i]))
            rect.setOutline("blue")
            rect.setFill("cyan")
            rect.draw(win)