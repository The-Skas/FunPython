#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ali
#
# Created:     21/02/2015
# Copyright:   (c) Ali 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import pdb
class Scene(object):
    def __init__(self):

        self.is_light_on = False
        self.contentsOfScene = ["door"]


    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Intro(Scene):
    def __init__(self):
        #here we would load all doors, items etc
        pass

    def _whileNotPressed(self,x,key,event):
        while x != key:
            x = raw_input(event).lower()

    def enter(self):
        print("You approach a house...")
        print("You see the main door...")
        x = ""
        self._whileNotPressed(x,"c", "Hit C to continue")
        self.corridor()

    def corridor(self):
        print("You have walked into a corridor with 2 rooms.")
        print("Do you go into room 1 or room 2?")
        x = ""
        x = raw_input("Enter 1 for room 1 and enter 2 for room 2 \n")
        if x == "1":
            Room1().enter()
        elif x == "2":
            Room2().enter()
        else:
            print("You did not enter 1 or 2")
            time.sleep(2)
            self.corridor()



class Room1(Scene):
    def __init__(self):
        #here we would load all doors, items etc
        super(Room1, self).__init__()
        self.cabinet = ['key', 'knife']

        self.contentsOfScene = self.contentsOfScene +  self.cabinet

        if('lantern' in self.contentsOfScene):
            self.is_light_on = True
        else:
            self.is_light_on = False

    def enter(self):
        print("You enter a room with a cabinet and a bed. ...")
        print("There are 1 doors in this room. One door to the east")


class Room2(Scene):
    def __init__(self):
        #here we would load all doors, items etc
        light ="dark"
        contentsOfScene = ["lantern"]
        exits = {'door1': 'locked'}

    def enter(self):
        print("You enter a room with a cabinet and a bed. ...")
        print("There are 1 doors in this room. One door to the east")

class Player(object):
    def __init__():
        self.inventory = []

    def pickup(item):
        pass


    def use(item):
        """ 
            A player can use an item (interact with it)
            ....
        """
        pass
intro = Intro()
intro.enter()
pdb.set_trace()