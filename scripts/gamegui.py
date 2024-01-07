# gamegui.py

from scripts.graphics import *
from scripts.matchapp import MatchApp
from scripts.boxview import BoxView
from scripts.imageview import ImageView
from scripts.startgame import StartGame


class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Match Me", 850, 777)
        self.win.setBackground("white")

        # banner
        banner = Text(Point(430, 45), "Match Me")
        banner.setSize(30)
        banner.setFill("brown")
        banner.setFace("courier")
        banner.setStyle("bold")
        banner.draw(self.win)

        # boxes
        BoxView(self.win)

        # images
        ImageView(self.win)

        # start button
        self.rect = Rectangle(Point(25, 715), Point(100, 745))
        self.rect.setFill("yellow")
        self.rect.draw(self.win)

        self.startbutton = Text(Point(61, 730), "START")
        self.startbutton.setSize(14)
        self.startbutton.setFace("courier")
        self.startbutton.setFill("brown")
        self.startbutton.draw(self.win)

        # quit button
        self.rect = Rectangle(Point(750, 715), Point(825, 745))
        self.rect.setFill("pink")
        self.rect.draw(self.win)

        self.qbutton = Text(Point(788, 730), "QUIT")
        self.qbutton.setSize(14)
        self.qbutton.setFace("courier")
        self.qbutton.setFill("brown")
        self.qbutton.draw(self.win)

    def close(self):
        self.win.close()

    def show(self):
        StartGame(self.win)

    def setSButton(self, btn, size):
        self.startbutton.setText(btn)
        self.startbutton.setSize(size)
