# Author: CRS 03/17/22
# Import turtle
import turtle

# Create the window
window = turtle.Screen()
window.setup(1000, 1000)
window.title("Lab 1")
steve = turtle.Turtle()
# Direct the turtle
steve.right(90)
steve.forward(250)
steve.left(90)
steve.forward(100)
steve.left(90)
steve.forward(250)
steve.left(90)
steve.forward(100)
# Make sure the window doesn't close
window.mainloop()