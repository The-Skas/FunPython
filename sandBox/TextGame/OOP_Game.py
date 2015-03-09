"""
    Build your own text game!
"""



from game_setup import *

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

    # Here we create the item 'stone'
    stone = dungeon.create_item("stone")

    # This means we don't want the player to pick up 
    # the item (not to be added to player's inventory).
    stone.can_pickup = False

    chain = dungeon.create_item("chain")

    # What happens when we use it in combination
    # with another item.
    stone.on_use(use_with="chain",  
        msg="You smash the stone on the chains breaking them! You can move.",
        action="player.can_move = True")


    basement = create_room("Basement")
    basement.description = "You enter a dark damp basement."


    # we set a value called player can_move to False.
    # TODO: seems complicated abstract more.
    player.can_move = False
    dungeon.connects_to(basement,
        through_dir = SOUTH,
        # When this condition is true, we can move.
        condition = "player.can_move == True",
        msg_on_true = "",
        msg_on_false = "I can't move because of the chains!")


    game_complete = create_room("You win!")
    game_complete.description = "You escape! You win!"
    basement.connects_to(game_complete, through_dir=EAST)

    player.start_game()
    # Start game.

main()





