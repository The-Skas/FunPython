import time
import pdb

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Room(object):
    _all_rooms = []

    @classmethod
    def setup(self):
        for room in self._all_rooms:
            room_description = room.description

            new_description = ""
            for word in room_description.split(" "):
                new_word = word

                start_bracket = word.find("{")
                end_bracket = word.find("}")

                if start_bracket >= 0 and end_bracket >= 0:
                    #get word between curly bracked {word here}
                    
                    item_name = word[start_bracket + 1:end_bracket]

                    item = room.get_item_in_room(item_name) \
                            or player.item_in_inventory(item_name)



                    if(item):
                        new_word = word.replace('{'+item_name+'}', str(item))

                new_description += new_word + " "

            room.description = new_description
    @classmethod
    def get_room_by_name(self, room_name):
        for room in self._all_rooms:
            if room.room_name == room_name:
                return room

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


    def remove_item_from_room(self, item):
        try:
            item_index = self.contents_of_scene.index(item)

            self.contents_of_scene.pop(item_index)
            return True
        except ValueError:                
            return False

    def connects_to(self, a_room, through_dir=0, condition='True',
            msg_on_true="", msg_on_false="" ):
        

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



        self.on_use_destroy = True
        self.description = ""
        # Intialise msgs
        self.on_pickup()
        self.on_use()
        self.on_use_with()

    def use_with(self):
        #Set a method name to a self. name
        prettyprint(self.use_with_pass_msg)
        exec(self.use_with_action)



    def on_use_with(self, use_with=None, action='None', 
      pass_msg = None,
      fail_msg = "I can't use it with that."):
        self.use_with_item = use_with
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




    def __str__(self):
        return bcolors.OKBLUE + self.name + bcolors.ENDC


class Player(object):

    def __init__(self, starts_in=None):
        self.current_room = starts_in
        self.inventory = []
        self.has_won = False
        self.health = 100

    def input_word_to_dir(self,_dir):
        _dir = _dir.upper()


        if _dir in DIRECTIONS:
            return _dir
        if "NORTH" in _dir:
            return "N"
        elif "SOUTH" in _dir:
            return "S"
        elif "EAST" in _dir:
            return "E"
        elif "WEST" in _dir:
            return "W"
        else:
            return ""


    def starts_in(self,room):
        self.current_room = room

    def start_game(self):
        Room.setup()
        print self.current_room.description
        while(not self.has_won):
            if self.health <= 0:
                prettyprint("You died.")
                return 

            self.input_action(raw_input(" > "))

    def change_room(self, room):
        if isinstance(room, str):
            room= Room.get_room_by_name(room)

        self.current_room = room

        prettyprint(self.current_room.description)

    def move(self, _dir):
        try:
            pdb.set_trace()

            _room = self.current_room.connected_rooms[_dir.upper()]

            if eval(_room['condition']):
                prettyprint(_room['msg_on_true'])
                return _room['room']
            else:
                prettyprint(_room['msg_on_false'])
                

        except KeyError:
            prettyprint("There is no path in that direction.")
        
        return None

    def pick_up(self,item):
        if item.can_pickup:
            # print msg
            self.inventory.append(item)
            self.current_room.contents_of_scene.remove(item)

            print item.pickup_pass_msg
            
            # The action to be performed when we pick up
            # an item. an example would be:
            #       Player.death = True
            #  
            exec(item.pickup_action)
        else:
            print item.pickup_fail_msg
    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        try:
            item_index = self.inventory.index(item)

            self.inventory.pop(item_index)
            return True
        except ValueError:
            return False

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

    def use_with(self, item1, item2):

        is_usable_with = item1.use_with_item and \
          item1.use_with_item.name == item2.name


        is_usable_with_reverse = item2.use_with_item and \
          item2.use_with_item.name == item1.name


        if is_usable_with:
            item1.use_with()
            return True
        elif is_usable_with_reverse:
            item2.use_with()
            return True
        else:
            prettyprint(item1.use_with_fail_msg)
            return False


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
       # [ word1, word2... wordn]


       # 'move  ' -> 'move'
        arr_input = [x.strip() for x in arr_input]
        # Now is the first Letter move?
        # if so go in
        if("move" in arr_input[0::1] and arr_input[1::2]):
            _dir = self.input_word_to_dir(arr_input[1::2][0])

            if(_dir):
                new_room = self.move(_dir)
                if(new_room):
                    self.change_room(new_room)
            else:
                prettyprint("In which direction should I move?")

        elif("pickup" in arr_input[0::1]):
            item = None
            try:
                item = arr_input[INDEX_ITEM]
                item = self.current_room.get_item_in_room(item)

                # If the item exists
                if item:
                    self.pick_up(item)
                else:
                    prettyprint("I don't see that anywhere here.")
            except Exception, e:
                prettyprint("What should I pickup?")

        elif("use" in arr_input[0::1] and "with" not in arr_input[2::3]):   
            try:
                item_name = arr_input[INDEX_ITEM]
                item = self.item_in_inventory(item_name) \
                        or self.current_room.get_item_in_room(item_name)
            
    
                if item:
                    self.use_item(item)
                elif not item:
                    prettyprint("I don't have that anywhere.")
            except Exception, ex:
                prettyprint("What should I use?")

            # Perform use operation.
        elif("use" in arr_input[0::1] and "with" in arr_input[2::3]):

            item_name = arr_input[INDEX_ITEM]
            item = self.item_in_inventory(item_name) \
                        or self.current_room.get_item_in_room(item_name)
            
            item_with_name = arr_input[INDEX_ITEM_WITH]
            item_with = self.item_in_inventory(item_with_name) \
                        or self.current_room.get_item_in_room(item_with_name)


            if item and item_with:
                is_success= self.use_with(item, item_with)

                if(is_success):
                    if item.on_use_destroy:
                        self.current_room.remove_item_from_room(item) \
                            or self.remove_item_from_inventory(item)

                    if item_with.on_use_destroy:
                        self.current_room.remove_item_from_room(item_with) \
                            or self.remove_item_from_inventory(item_with)




        
            elif not item.use_with_item:
                print "I cant use that with anything."

                
        elif("inventory" in arr_input[0::1]):
            # If player has nothing
            if not self.inventory:
                prettyprint("I have nothing in my inventory.")
            else:
                prettyprint("Your Inventory:")
                for item in self.inventory:
                    prettyprint("  "+item.name)

        elif("look" in arr_input[0::1] and not arr_input[1::2]):
            prettyprint(self.current_room.description)

        elif("look" in arr_input[0::1] and arr_input[1::2]):
            item = None
            
            item = arr_input[INDEX_ITEM]
            item = self.current_room.get_item_in_room(item)

            # If the item exists
            if item:
                prettyprint(item.description)
            else:
                prettyprint("I don't see that anywhere here.")
    
        elif(_input.find("?") != -1 
            or _input.find("help") != -1):
            print help_msg()
        else:

            prettyprint("I don't understand that.")
            prettyprint("Type '?' or 'help'")

        return self.current_room
  



# List of all rooms
def create_room(_room_name, action = None):
    room_names = [room.room_name for room in Room._all_rooms]
    # The room Doesnt exist
    if _room_name not in room_names:
        new_room = Room(_room_name)
        Room._all_rooms.append(new_room)

        return new_room
    else:
        return Room.get_room_by_name(_room_name)
        # raise TypeError("The room:",room,"already exists!")

def create_item(item, in_room = None, in_player_inventory = False):
    if in_player_inventory:
        _item = Item(item, None)
        player.inventory.append(_item)

        return _item
    elif in_room:
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

        look : describes the room you are in.

        look [item_name] : describes the item you are looking at.
            """
def prettyprint(_str, indent = 2):
    arr = _str.split("\n")

    for line in arr:
        print " "*indent +line
# DEBUG
DEBUG = False


DIRECTIONS = ["N","S","E", "W"]
SOUTH = "S"
NORTH = "N"
EAST  = "E"
WEST  = "W"

# INDICES:
INDEX_ACTION = 0
INDEX_ITEM = 1
INDEX_WITH = 2
INDEX_ITEM_WITH = 3


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

