import random
import time
from top_secret import computer

# Alright hackers, we need to hack into the computer.
# To do that, we need to figure out its password!
# 
# To hack the computer input the following command.
# 
# 	  computer.guess_password("put what you think is the password here!")
# 
# 
# HINT: the computer password is a number between 1 and 100000
# 
# You have to be fast! 
# 


# Hmmm.. There must a better way than typing it all out!
# what if i use loops?
computer.guess_password(1337)
computer.guess_password(5555)
computer.guess_password(645)


_pass = 0
while(True):
	_pass += 1
	computer.guess_password(_pass)



