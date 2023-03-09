# matchapp.py



class MatchApp:

    def __init__(self, interface):
        self.interface = interface

    def run(self):
        while True:
            clicks = self.interface.win.getMouse()
            if (25 <= clicks.getX() <= 100) and (715 <= clicks.getY() <= 745):
                print("Game Start!")
                self.interface.setSButton("RESTART", 10)
                self.interface.show()
                break
            if (750 <= clicks.getX() <= 825) and (715 <= clicks.getY() <= 745):
                print("Game Closed!")
                self.interface.win.close()
                break