# Author: CRS 03/21/22
# Import turtle
import turtle

# Define move functions
def move_backward():
    toby.back(50)
def turn_right():
    toby.right(90)
def turn_left():
    toby.left(90)
# Make turtle move
window = turtle.Screen()
toby = turtle.Turtle()
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.listen()
window.mainloop()
