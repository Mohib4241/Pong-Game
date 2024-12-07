from time import sleep
from turtle import Turtle, Screen



class Screen_Setup():

    def __init__(self):
        # Create a screen instance
        self.screen = Screen()
        self.screen.bgcolor("black")  # Set background color of the screen
        self.screen.setup(width=800, height=600)  # Set screen size

        # Create a turtle instance
        self.turtle = Turtle()
        self.screen.tracer(0)
        self.turtle.width(2)
        self.turtle.pencolor("white")
        self.turtle.fillcolor("white")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(0, 370)
        self.turtle.right(90)

        # Draw the pattern with the turtle
        for _ in range(37):
            self.turtle.forward(10)
            self.turtle.penup()
            self.turtle.forward(10)
            self.turtle.pendown()

        self.screen.update()
        sleep(0.1)

# s = Screen_Setup()/