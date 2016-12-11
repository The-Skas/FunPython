from turtle import *
import math
shape("turtle")
speed(0)

def triangle(x, y, side):
    penup()
    setpos(x,y)
    pendown()
    seth(60)
    for x in range(3):
        forward(side)
        right(120)
        
def recTriangle(x,y,size):
    if(size <= 5):
        return 0;

    triangle(x,y, size)
    
    leftX = x
    leftY = y
    recTriangle(leftX, leftY, size/2)

    topX = x + cos(math.radians(60))*(size/2)
    topY = y + sin(math.radians(60))*(size/2)
    recTriangle(topX, topY, size/2)

    rightX = x + size/2
    rightY = y
    recTriangle(rightX, rightY, size/2)


def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
 
# f(500, 5)

recTriangle(-200,-200,500.0)
    
