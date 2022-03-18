# Author: CRS 03/18/22
# Import turtle
from email.policy import default
import turtle

# Create the window
window = turtle.Screen()
window.title("Lab 4")
alfonso = turtle.Turtle()
alfonso.speed(5)
alfonso.pencolor("purple")
alfonso.stamp()
alfonso.setposition(100, 100)

# Create goto
alfonso.begin_fill()
alfonso.goto(100, 0)
alfonso.goto(0, 0)
alfonso.goto(0, 100)
alfonso.goto(100, 100)
alfonso.end_fill()

# Make sure the window doesn't close
window.mainloop()
