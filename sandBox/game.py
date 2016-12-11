import time

class Scene(object):
    def __init__(self):
        pass
        
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
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
        pass
        
    def enter(self):
        print("You enter a room with a cabinet and a bed. ...")
        print("There are 1 doors in this room. One door to the east")


class Room2(Scene):
    def __init__(self):
        #here we would load all doors, items etc
        pass
        
    def enter(self):
        print("You enter a room with a cabinet and a bed. ...")
        print("There are 1 doors in this room. One door to the east")

        
intro = Intro()
intro.enter()
