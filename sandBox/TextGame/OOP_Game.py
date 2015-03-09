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

DIRECTIONS = ["N","S","E", "W"]
SOUTH = "S"
NORTH = "N"
EAST  = "E"
WEST  = "W"

class Room(object):
    def __init__(self, name):
        self.room_name = name.lower()

        self.description = "No description Entered."

        # Items available
        self.contents_of_scene = []

        # What it connects to
        self.connected_rooms = {}

    def enter(self):
        print(self.description)
    
    def create_item(self,item):
        _item = Item(item, self.room_name)
        self.contents_of_scene.append(_item)
        return _item

    def look_up_item_in_room(self, _item):
        item_names = [item.name for item in self.contents_of_scene]
        if(_item in item_names):
            return self.contents_of_scene[item_names.index(_item)]
        else:
            return None

    def connects_to(self, a_room, through_dir=0, condition='True',
            msg_on_true=None, msg_on_false=None ):
        

        a_room_exists = isinstance(a_room,Room)
        a_valid_dir   = DIRECTIONS.__contains__(through_dir)
        if(a_room_exists and a_valid_dir):
            self.connected_rooms[through_dir] = {}
            self.connected_rooms[through_dir]["room"] = a_room

            if(condition):
                self.connected_rooms[through_dir]['condition'] = condition
                self.connected_rooms[through_dir]['msg_on_true']  =  msg_on_true
                self.connected_rooms[through_dir]['msg_on_false'] = msg_on_false

        if(not a_valid_dir):
            raise TypeError("Invalid Direction!")
        if(not a_room_exists):
            raise TypeError("Invalid Room!")

class Item(object):
    def __init__(self, item_name, room_name):
        self.name = item_name
        self.found_in_room = room_name
        self.can_pickup = True
        self.can_use = False

    def on_use(self, use_with=None, action=None, msg="I can't use that."):
        self.use_with = use_with
        self.action = action
        self.msg = msg






class Player(object):

    def __init__(self, starts_in):
        self.current_room = starts_in

    def start_game(self):
        print self.current_room.description
        while(True):
            self.input_action(raw_input(" > "))

    def input_action(self,_input):
 
        if(_input.upper() in DIRECTIONS):
            # Evaluate movement
            current_room = self.current_room
            move_dir = _input.upper()
            connected_rooms = self.current_room.connected_rooms
            if(connected_rooms.has_key(move_dir)):

                dict_dir = connected_rooms[move_dir]

                room_object = dict_dir["room"]

                if(eval(dict_dir["condition"])):
                    if(dict_dir["msg_on_true"]):
                        print dict_dir["msg_on_true"]
                    # Return new room to go to
                    print room_object.description
                    return room_object
                else:
                    print dict_dir["msg_on_false"]
        # 
        # **USE***
        # 
        item_message =_input.lower().split(" ")
        if(_input.find("use") == 0 and 
            len(item_message) > 1):
            item_message =_input.split(" ")

            item = self.current_room.look_up_item_in_room(item_message[1])
            if(not item):
                return self.current_room
            # Found item in current room
            # Either use, or use with combination.
            # UGLY CODE!
            if(len(item_message) == 4):
                _with = item_message[2]
                item_2 = item_message[3]

                if(_with == "with"):
                    _item_2 = self.current_room.look_up_item_in_room(item_2)
                    
                    if(not _item_2):
                        return self.current_room
                    if(_item_2 and item_2 == item.use_with):
                        exec(item.action)
                        print(item.msg)

            elif(not item.use_with):
                exec(item.action)
                print(item.msg)






        if(_input.find("?") != -1
            or _input.find("help") != -1):
            print """
            Available Actions: 
                move:(example)
                     move N,     move S,     move E,    move W
                     move North, move South, move East, move West

                pickup [item_name]: picks up an item if possible, 
                                    adding it to inventory.

                use [item_name]: uses an item.

                use [item_name] with [item_name]: uses items together
            """
        return self.current_room
    
# List of all rooms
_rooms = []
def create_room(_room_name):
    room_names = [room.room_name for room in _rooms]
    # The room Doesnt exist
    if _room_name not in room_names:
        new_room = Room(_room_name)
        _rooms.append(new_room)
        return new_room
    else:
        raise TypeError("The room:",room,"already exists!")




# An example of user created content.
# 
# This creates a Room. We name it 'Dungeon'
dungeon = create_room("Dungeon_Cell")


player = Player(starts_in=dungeon)

# Here we add the description for the dungeon.
dungeon.description = """
You wake up.
    
Dark grey crumbling walls enclose your surroundings. A dark door
is to the South of you. You try to move but your legs are locked 
in iron 'chain'.

'Help!', you yell with all your strength, but only the echo 
of your own voice greets you. In anger, you hit the wall and a 
chunk of 'stone' falls next to you."""

# Here we create the item 'stone'
stone = dungeon.create_item("stone")

# This means we don't want the player to pick up 
# the item (not to be added to player's inventory).
stone.can_pickup = False

chain = dungeon.create_item("chain")
# What happens when we use it with another item.
stone.on_use(use_with="chain",  
    msg="You smash the stone on the chains breaking them! You can move.",
    action="player.can_move = True")


basement = create_room("Basement")
basement.description = "You enter a dark damp basement."


# we set a value called player can_move
player.can_move = False
dungeon.connects_to(basement,
    through_dir = SOUTH,
    condition = "player.can_move == True",
    msg_on_true = "",
    msg_on_false = "I can't move because of the chains!")


game_complete = create_room("You win!")
game_complete.description = "You escape! You win!"
basement.connects_to(game_complete, through_dir=EAST)

player.start_game()
# Start game.







