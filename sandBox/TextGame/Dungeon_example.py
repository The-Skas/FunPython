"""
    Build your own text game!
"""



from game_setup import *


    # Make sure different items have different names!
    # 
    # 
    # An example of user created content.
    # 
    # Please play the complete game by running
    # 'python OOP_Game.py' before reading further.

def main():
    # This creates a Room. We name it 'Dungeon Cell'
    # We store it in a variable called 'dungeon'
    dungeon = create_room("Dungeon Cell")

    # Here we choose what room the player starts in!
    # In this case 
    player.starts_in(dungeon)

    # Here we add the description for the dungeon.
    # This is what is printed to the screen when the
    # player enters the dungeon.
    # 
    # {item_name} describes the item in the room. Do
    # this if you wan't the item to be highlighted!
    # 
    # TODO: Add one time only messages. Such as events.
    # For example here the event would be a rock
    # falling. It shouldn't be repeated.

    dungeon.description = """
    You wake up.
        
    Dark grey crumbling walls enclose your surroundings. A dark door
    is to the South of you. You try to move but your legs are locked 
    in iron {chain}.

    'Help!', you yell with all your strength, but only the echo 
    of your own voice greets you. In anger, you hit the wall and a 
    chunk of {stone} falls next to you."""

    # Here we create the item 'stone', placing it
    # inside the dungeon room!
    stone = create_item("stone", in_room = dungeon)

    stone.description = """
    A grey heavy stone, hmmm.. maybe I can use this somehow.
    """
    # This means the player can't pick up the item
    # stone.can_pickup = False

    # Here we give the message when the player trys to pickup.
    # notice we have 'fail_msg' with a value.

    # The 'fail_msg' is displayed
    # if the player fails to pick up the stone.
    # 
    # the 'pass_msg' is displayed if the player
    # can pick up the message.
    # 
    # Since 'stone.can_pickup = False'
    # the player will get the 'fail_msg'
    # 
    # If we change it to 'stone.can_pickup = True'
    # then the player will get the pass_msg

    stone.can_pickup = False
    stone.on_pickup(fail_msg = "That stone is too large to fit in my inventory..\n but maybe I can still use it.",
                    pass_msg = "I am so Strong! picking up this stone is easy!")

    stone.on_use(fail_msg = "Using the stone with something will be more helpful.")

    # We add the item 'chain' to the player inventory.
    # Notice we did not add in_room. Thats because
    # we don't wan't the item in the room, but only
    # in the players inventory!
    # player will be chained - 
    # sinces hes a prisoner in a dungeon! :O
    chain = create_item("chain", in_player_inventory = True)
    chain.on_use(fail_msg = "Perhaps I can use it with something.")


    # We create another room
    basement = create_room("Basement")
    basement.description = "You enter a dark damp basement. "+ \
                           "The pungent air crawls up through your nostrils."+ \
                           " You can hear the faint screams of prisoners coming from"+ \
                           " all around. \n\n"+ \
                           "Infront of you is a {door} with the sign - 'EXIT'."


    door = create_item("door", in_room = basement)
    door.can_use = True
    door.on_use(pass_msg = "You escape the dungeon!", action="player.has_won = True")

    door.on_pickup(fail_msg="I can't pick up a door! Are you mad?")
    # we set a value called player can_move to False.

    player.can_move = False
    #Here, we connect the basement to the dungeon.
    dungeon.connects_to(basement,
        through_dir = SOUTH,
        # When the chain not in the player's inventory
        condition =  "player.can_move == True",
        msg_on_true = "",
        msg_on_false = "I can't move while im in chains!")


    # What happens when we use 'stone' in combination
    # with 'chain'.
    #       use_with: this is the item to use with
    #       pass_msg: the message that is printed when we successfully
    #                 use 'stone' with 'chain'
    #       action:   the action that will happens, in this case we 
    #                 set 'player.has_chains = True'
    stone.on_use_with(use_with=chain,
                    pass_msg="You smash the stone on the chains breaking them! You can move.",
                    fail_msg ="You can't use it like that..",
                    action="player.can_move = True")
    

#----DO NOT EDIT BELOW THIS---
main()
# Start game.
player.start_game()






