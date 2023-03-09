from graphics import *
from random import *

class ImageView:

    def __init__(self, win):
        self.win = win
        self.imglist = ["beads.png", "design.png", "earth_hand.png", "interesting.png", "jellyfish.png",
                        "owl_drawing.png",
                        "pokeball.png", "show.png", "skeleton.png", "universe_water.png"]

        self.imglistcopy = ["beads.png", "design.png", "earth_hand.png", "interesting.png", "jellyfish.png",
                            "owl_drawing.png", "pokeball.png", "show.png", "skeleton.png", "universe_water.png"]
        self.randlist = []
        self.randlistcopy = []

        self.imgbutton = []
        self.imgbuttoncopy = []

        self.all = []
        self.points = []

        self.xlist = []
        self.ylist = []
        y = 168

        # image coordinates
        for col in range(4):
            x = 118
            for row in range(5):
                self.xlist.append(x)
                self.ylist.append(y)
                x += 155
            y += 145

        # plotting the images
        for i in range(len(self.xlist)):
            while True:
                randimg = self.imglist[int(random()*10)]
                randimgcopy = self.imglistcopy[int(random() * 10)]

                if randimg not in self.randlist:
                    self.randlist.append(randimg)
                    self.all.append(randimg)
                    img = Image(Point(self.xlist[i], self.ylist[i]), randimg)
                    self.imgbutton.append(img)
                    self.points.append(img.getAnchor().getX() + img.getAnchor().getY())
                    break
                elif randimgcopy not in self.randlistcopy:
                    self.randlistcopy.append(randimgcopy)
                    self.all.append(randimgcopy)
                    img = Image(Point(self.xlist[i], self.ylist[i]), randimgcopy)
                    self.imgbuttoncopy.append(img)
                    self.points.append(img.getAnchor().getX() + img.getAnchor().getY())
                    break
                else:
                    continue


