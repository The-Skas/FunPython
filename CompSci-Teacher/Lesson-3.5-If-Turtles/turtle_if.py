from turtle_setup import *
import turtle

# ************************************************************************
# Excercise:
# ----------
# Goal: Make a turtle move around the screen with your keyboard!
# 
# Look at 'key_pressed'
# 
# What you will need to do is use, if and elif to see what key
#       the user is pressing. In this case, look for the arrow keys.
#       
# 
#        HINT: Arrow keys are: Up - Down - Left - Right
# 
# ************************************************************************


def key_pressed(keypress):
    
	# As we can see, here we do an if check for the 'Up' arrow key.
	# add in the rest to make the turtle move using all the arrow keys!
	# 
	#               Fix the WRONG code below!
	#
	
    if(keypress.keysym == "Up"):
        turtle.forward(10)
        turtle.backward(10)
    elif(2 == 1):
    	turtle.forward(0)

        










# ***********************************
# Don't worry about whats below here.
# Look above at 'key_pressed'
# ***********************************

if __name__ == "__main__":
    setup("blue",-200,200,2,2,"turtle")

