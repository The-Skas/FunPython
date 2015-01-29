from turtle_if import key_pressed
import turtle
# from turtle_if import key_pressed
wn = turtle.Screen()

def setup(col, x, y, w, s, shape): 
    turtle.up()
    turtle.goto(x,y)
    turtle.width(w)
    turtle.turtlesize(s)
    turtle.color(col)
    turtle.shape(shape)
    turtle.bgpic("assets/dancing-banana.gif")
    turtle.down()
    wn.listen()
    turtle.getscreen()._root.bind_all('<Key>', key_pressed)
    turtle.getscreen()._root.mainloop()