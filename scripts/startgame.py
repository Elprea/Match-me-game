# startgame.py

from scripts.boxview import BoxView
from scripts.imageview import ImageView
import time


class StartGame:
    def __init__(self, win):
        self.win = win

        bview = BoxView(self.win)
        iview = ImageView(self.win)

        imgobjects = iview.imgbutton + iview.imgbuttoncopy
        p = []
        boxlist = []
        count = 0
        storepoint = 0
        point = 0
        imgpoints = {}

        for k in range(len(iview.all)):
            imgpoints[iview.points[k]] = iview.all[k]
            imgobjects[k].draw(self.win)
        time.sleep(0.5)
        for h in range(len(iview.all)):
            imgobjects[h].undraw()

        # Game loop
        while True:
            clicks = self.win.getMouse()
            compare = []
            buttondone = False

            # Restart Button
            if (25 <= clicks.getX() <= 100) and (715 <= clicks.getY() <= 745):
                StartGame(self.win)
                break

            # Quit Button
            if (750 <= clicks.getX() <= 825) and (715 <= clicks.getY() <= 745):
                print("Game Closed!")
                self.win.close()
                break
            if len(boxlist) != 0:
                for b in range(len(boxlist)):
                    if (boxlist[b][0] <= clicks.getX() <= boxlist[b][1]) and (boxlist[b][2] <= clicks.getY() <= boxlist[b][3]):
                        buttondone = True
                        break
                    else:
                        buttondone = False
            if buttondone == False:
                # If not Quit Button
                for j in range(20):
                    # If boxes clicked
                    boxpoints = [bview.x1list[j], bview.x2list[j], bview.y1list[j], bview.y2list[j]]
                    if (boxpoints[0] <= clicks.getX() <= boxpoints[1]) and (boxpoints[2] <= clicks.getY() <= boxpoints[3]):
                        for i in range(len(imgobjects)):
                            clickimg = imgobjects[i].getAnchor()
                            if (bview.x1list[j] <= clickimg.getX() <= bview.x2list[j]) and (bview.y1list[j] <= clickimg.getY() <= bview.y2list[j]):
                                imgobjects[i].draw(self.win)
                                storepoint = clickimg.getX() + clickimg.getY()
                                count += 1
                                break

                        if count == 1:
                            storepoint2 = storepoint
                            boxpointscopy = [bview.x1list[j], bview.x2list[j], bview.y1list[j], bview.y2list[j]]
                            point = i
                        else:
                            if (imgpoints[storepoint] == imgpoints[storepoint2]):
                                boxlist.append(boxpointscopy)
                                boxlist.append(boxpoints)
                                if len(boxlist)//2 == 1:
                                    print("Good Job! You got " + str(len(boxlist)//2) + " pair")
                                else:
                                    print("Good Job! You got " + str(len(boxlist) // 2) + " pairs")
                            else:
                                print("Not a pair!")
                                time.sleep(1)
                                imgobjects[point].undraw()
                                imgobjects[i].undraw()
                            count = 0
                        break

            if len(boxlist) == 20:
                print("""
            ░░█▀░░░░░░░░░░░▀▀███████░░░░ 
            ░░█▌░░░░░░░░░░░░░░░▀██████░░░ 
            ░█▌░░░░░░░░░░░░░░░░███████▌░░ 
            ░█░░░░░░░░░░░░░░░░░████████░░ 
            ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ 
            ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ 
            ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ 
            ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ 
            ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌         CONGRATULATIONS!!
            ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌           YOU COMPLETED IT!
            ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░              JOB WELL DONE!
            ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ 
            ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ 
            ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ 
            ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ 
            ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ 
            ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░           *Click Anywhere to EXIT
            ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ 
            ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ 
            ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ 
            ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ 
            ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ 
            ░░▄▌████████▄▄▄███████▌░░░░░▄ 
            ░▄▀░██████████████████▌▀▄░░░░ 
            ▀░░░█████▀▀░░░▀███████░░░▀▄░░ 
            ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ 
            ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ 
            ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ 
            ░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░ 
            ░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░ 
            ░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░ """)



'''
print(time.asctime())
>>Mon Aug 26 15:39:18 2019

print(time.gmtime())
>>time.struct_time(tm_year=2019, tm_mon=8, tm_mday=26, tm_hour=22, tm_min=41, tm_sec=27, tm_wday=0, tm_yday=238, tm_isdst=0)

time.sleep(num in seconds)
>> delay to execute next program
'''
