


from game_setup import *




space_cabin = create_room("space intro")

space_cabin.description = """
You have been abandonded on planet xorb.

Ahead of you, an enemy approaches. A big green gooey
{glob}, with eyes the size of plates. 

All you have in your inventory is your trusted
{zapper}.

What do you do?
"""

#Using an item to simulate an enemy.
glob = create_item("glob", in_room=space_cabin)

glob.on_use(fail_msg = "I won't touch that thing, gross!")
glob.can_use = False

glob.on_pickup(fail_msg = "What?! Pick up that slimeball?! No way!")
glob.can_pickup = False




zapper = create_item("zapper", in_player_inventory=True)

zapper.on_use_with(use_with=glob,
				 pass_msg="You shoot the big glob in the face! It drops a key.",
				 action='player.change_room("space glob attack")')

player.starts_in(space_cabin)

s

player.start_game()




