import time
import pdb


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

    def get_item_in_room(self, _item):
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
        self.can_pickup = False
        self.can_use = False

        # Intialise msgs
        self.on_pickup()
        self.on_use()
        self.on_use_with()

    def on_use_with(self, use_with=None, action='None', 
      pass_msg = None,
      fail_msg = "I can't use it with that."):
        self.use_with = use_with
        self.use_with_action = action
        self.use_with_fail_msg = fail_msg
        self.use_with_pass_msg = pass_msg


    def on_use(self, action='None', 
      pass_msg = None,
      fail_msg    = "I can't use that."):
        self.use_action = action
        self.use_msg_fail = fail_msg
        self.use_msg_pass = pass_msg
        if not pass_msg:
            self.use_msg_pass = "used "+self.name

    def on_pickup(self, action='None',
      pass_msg = None,
      fail_msg    = "I can't pick that up"):
        self.pickup_action = action
        self.pickup_fail_msg = fail_msg
        self.pickup_pass_msg = pass_msg

        if not pass_msg:
            self.pickup_pass_msg = "picked up "+self.name





class Player(object):

    def __init__(self, starts_in=None):
        self.current_room = starts_in
        self.inventory = []

    def starts_in(self,room):
        self.current_room = room

    def start_game(self):
        print self.current_room.description
        while(True):
            self.input_action(raw_input(" > "))

    def pick_up(self,item):
        if item.can_pickup:
            # print msg
            self.inventory.append(item)
            print item.pickup_pass_msg
            
            # The action to be performed when we pick up
            # an item. an example would be:
            #       Player.death = True
            #  
            exec(item.pickup_action)
        else:
            print item.pickup_fail_msg

    def use_item(self,item):
        if item.can_use:
            for _item in self.inventory:
                if _item.name.lower() == item:
                    self.inventory.remove(_item)
                    if DEBUG: print "--Successfully Removed."

            print item.use_msg_pass

            # The action to be performed when we use
            # an item. an example would be:
            #       Player.death = True
            #  
            exec(item.use_action)
        else:
            print item.use_msg_fail


    def item_in_inventory(self, item):

        for _item in self.inventory:
            if _item.name.lower() == item:
                
                if DEBUG: print "--Found item in inv"
                return _item

        if DEBUG: print "--Couldnt find in Inv."
        return None

    def input_action(self,_input):
    
        # Here I split it
        arr_input = _input.lower().split(" ")
       
        # Now is the first Letter move?
        # if so go in
        if("move" in arr_input[0::1]):
            pass
            # Then first check, if move alone,
            # then throw a help msg!
            #   
        elif("pickup" in arr_input[0::1]):
            item = None
            try:
                item = arr_input[INDEX_ITEM]
                item = self.current_room.get_item_in_room(item)

                # If the item exists
                if item:
                    self.pick_up(item)
                else:
                    print "I don't see that anywhere here."
            except Exception, e:

                print "What should I pickup?"
        elif("use" in arr_input[0::1] and "with" not in arr_input[2::3]):   
            try:
                item_name = arr_input[INDEX_ITEM]
                item = self.item_in_inventory(item_name)
                if item:
                    self.use_item(item)
            
                item = self.current_room.get_item_in_room(item_name)
                if item:
                    self.use_item(item)

                if not item:
                    print "I don't have that anywhere."
            except Exception, ex:
                print "What should I use?", ex

            # Perform use operation.
        elif("use" in arr_input[0::1] and "with" in arr_input[2::3]):
            try:
                item_name = arr_input[INDEX_ITEM]
                item = self.item_in_inventory(item_name)
                
                item_with_name = arr_input[INDEX_ITEM_WITH]
                item_with = self.item_in_inventory(item_with_name)

                # if item and :
                #     self.use_with(item, )
                    
                # if not item.use_with:
                #     print "I cant use that with anything."

            except Exception, ex:
                print "What should I use it with?", ex
        elif("inventory" in arr_input[0::1]):
            # If player has nothing
            if not self.inventory:
                print "You have no inventory."
            else:
                print "Your Inventory:"
                for item in self.inventory:
                    print "  ",item.name

        elif(_input.find("?") != -1
            or _input.find("help") != -1):
            print help_msg()

        else:
            print "I don't understand that."
            print "Type '?' or 'help'"

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

def create_item(item, in_room):
    return in_room.create_item(item)

def help_msg():
        return """
    Available Actions: 
        move : (example)
              move N,     move S,     move E,    move W
              move North, move South, move East, move West

        pickup [item_name] : picks up an item if possible, 
                            adding it to inventory.

        use [item_name] : uses an item.

        use [item_name] with [item_name] : uses items together

        inventory : shows list of items in inventory

            """
# DEBUG
DEBUG = True


DIRECTIONS = ["N","S","E", "W"]
SOUTH = "S"
NORTH = "N"
EAST  = "E"
WEST  = "W"

# INDICES:
INDEX_ACTION = 0
INDEX_ITEM = 1
INDEX_WITH = 2
INDEX_ITEM_WITH = 4


player = Player()


 # if(_input.upper() in DIRECTIONS):
        #     # Evaluate movement
        #     current_room = self.current_room
        #     move_dir = _input.upper()
        #     connected_rooms = self.current_room.connected_rooms
        #     if(connected_rooms.has_key(move_dir)):

        #         dict_dir = connected_rooms[move_dir]

        #         room_object = dict_dir["room"]

        #         if(eval(dict_dir["condition"])):
        #             if(dict_dir["msg_on_true"]):
        #                 print dict_dir["msg_on_true"]
        #             # Return new room to go to
        #             print room_object.description
        #             return room_object
        #         else:
        #             print dict_dir["msg_on_false"]
        # # 
        # # **USE***
        # # 
        # item_message =_input.lower().split(" ")
        # if(_input.find("use") == 0 and 
        #     len(item_message) > 1):
        #     item_message =_input.split(" ")

        #     item = self.current_room.look_up_item_in_room(item_message[1])
        #     if(not item):
        #         return self.current_room
        #     # Found item in current room
        #     # Either use, or use with combination.
        #     # UGLY CODE!
        #     if(len(item_message) == 4):
        #         _with = item_message[2]
        #         item_2 = item_message[3]

        #         if(_with == "with"):
        #             _item_2 = self.current_room.look_up_item_in_room(item_2)
                    
        #             if(not _item_2):
        #                 return self.current_room
        #             if(_item_2 and item_2 == item.use_with):
        #                 exec(item.action)
        #                 print(item.msg)

        #     elif(not item.use_with):
        #         exec(item.action)
        #         print(item.msg)

