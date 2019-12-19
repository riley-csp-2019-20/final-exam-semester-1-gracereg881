#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Grace Regulinski
#Date
# 12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller                              
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#








#import required libraries
import turtle as trtl

#create turtle
ben = trtl.Turtle()
ben.turtlesize(1)
ben.pensize(1)


#movement functions

# moving up when pressing up arrow key
def up():
    ben.setheading(90)
    ben.forward(10)

# moving down when pressing down arrow key
def down():
    ben.setheading(270)
    ben.forward(10)

# moving right when pressing right arrow key
def right():
    ben.setheading(0)
    ben.forward(10)

# moving left when pressing left arrow key
def left():
    ben.setheading(180)
    ben.forward(10)

#color/drawing functions



# used to clear the drawing when space is pressed
def clear():
    ben.clear()

# used to make the pensize smaller when the o key is pressed
def pen_size_big():
    if ben.pensize(1):
        ben.pensize(2)
    if ben.pensize(2):
        ben.pensize(3)
    if ben.pensize(3):
        ben.pensize(4)
    if ben.pensize(4):
        ben.pensize(5)

def pen_size_small():
    if ben.pensize(5):
        ben.pensize(4)
    if ben.pensize(4):
        ben.pensize(3)
    if ben.pensize(3):
        ben.pensize(2)
    if ben.pensize(2):
        ben.pensize(1)

    

"""# used to pick pen up and put pen down
def pensetting():
    if ben.penup:
        ben.pendown()"""


#create screen

#bind to keypresses
wn = trtl.Screen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

wn.onkeypress(clear, "space")

wn.onkeypress(pen_size_big, "o")

wn.onkeypress(pen_size_small, "p")

"""wn.onkeypress(pensetting, "u")"""

#listen
wn.listen()

#mainloop
wn.mainloop()