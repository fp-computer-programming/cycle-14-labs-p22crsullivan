# Author: CRS 03/21/22
# Import turtle
from email.policy import default
import turtle

# Ask for input
color = turtle.textinput("color", "Enter a color.")
size = turtle.numinput("size", "Enter a size from one to five.", None, 1, 5)

# Create turtle
window = turtle.Screen()
toby = turtle.Turtle()
toby.color(color)
toby.shapesize(size)

# Define function
def on_clk():
    toby.forward(100)
    toby.left(90)
    toby.forward(100)
    toby.left(90)
    toby.forward(100)
    toby.left(90)
    toby.forward(100)
    toby.left(90)

# Create onclick
turtle.onclick(on_clk(), btn = 1)
window.mainloop()
