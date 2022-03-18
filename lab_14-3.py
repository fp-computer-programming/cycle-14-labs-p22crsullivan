# Author: CRS 03/18/22
# Import turtle
import turtle

# Create the window
window = turtle.Screen()
window.setup(500, 500)
window.title("Lab 3")
jonathan = turtle.Turtle()
jonathan.shape("turtle")
jonathan.pencolor("purple")
window.bgcolor("grey")

# Create for loop
for x in range(200):
    jonathan.back(200)
    jonathan.left(120)

# Make sure the window doesn't close
window.mainloop()
