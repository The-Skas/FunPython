"""
    Build your own text game!
"""



from game_setup import *


# Make sure different items have different names!
# 
# 
def main():
    # An example of user created content.
    # 
    # This creates a Room. We name it 'Dungeon'
    dungeon = create_room("Dungeon_Cell")

    # This is the room the player starts in.
    player.starts_in(dungeon)
    # Here we add the description for the dungeon.
    dungeon.description = """
    You wake up.
        
    Dark grey crumbling walls enclose your surroundings. A dark door
    is to the South of you. You try to move but your legs are locked 
    in iron 'chain'.

    'Help!', you yell with all your strength, but only the echo 
    of your own voice greets you. In anger, you hit the wall and a 
    chunk of 'stone' falls next to you."""

    # Here we create the item 'stone', placing
    # inside the dungeon room!
    stone = create_item("stone", in_room = dungeon)

    # This means the player can't pick up the item
    stone.can_pickup = False
    # Here we give the message when the player trys to pickup.
    # notice we have 'fail_msg' with a value
    stone.on_pickup(fail_msg = "That stone is too heavy.. "+
                               "maybe I can use it with something.")

    
    chain = create_item("chain", in_room = dungeon)
    
    chain.can_pickup = False


    # We create another room
    basement = create_room("Basement")
    basement.description = "You enter a dark damp basement. \n"+ \
                           "The pungent air crawls up through your nostrils"+ \
                           "You can hear the faint screams of prisoners coming from"+ \
                           "south."



    # we set a value called player can_move to False.
    
    player.can_move = False

    #Here, we connect the basement to the dungeon.
    #But as you can see..
    dungeon.connects_to(basement,
        through_dir = SOUTH,
        # When this condition is true, we can go to the basement.
        condition = "player.can_move == True",
        msg_on_true = "",
        msg_on_false = "I can't move because of the chains!")

    # What happens when we use 'stone' in combination
    # with 'chain'.
    #       use_with: this is the name of the item
    #       pass_msg: the message that is printed when we successfully
    #                 use 'stone' with 'chain'
    #       action:   the action that will happens, in this case we assign
    #                 player.can_move = True
    stone.on_use_with(use_with="chain",
                    pass_msg="You smash the stone on the chains breaking them! You can move.",
                    action="player.can_move = True")


    game_complete = create_room("win")
    game_complete.description = "You escape the dungeon!"
    basement.connects_to(game_complete, through_dir=EAST)

    player.start_game()
    # Start game.

main()





