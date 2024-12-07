from select import select
from time import sleep
from  random import randint
from turtle import Turtle,Screen
from turtledemo.clock import setup


# from pythonProject1.main import screen
# #
# scren = Screen()
# scren.bgcolor("black")

class Ball(Turtle):

    # count = 0
    def __init__(self,shape="circle",color="white"):
        super().__init__()
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()
        self.penup()
        # self.speed("slow")
        self.penup()
        self.color(color)
        self.shape(shape)
        self.x_move = 10
        self.y_move = 10


    def start(self):

        self.x_pos = self.xcor() +  self.x_move
        self.y_pos = self.ycor() +  self.y_move
        self.goto(self.x_pos ,self.y_pos)

    def collision_with_wall(self):
        self.y_move *= -1


    def collision_with_X_bounce(self):
        self.x_move *= -1

    def collision_with_Y_bounce(self):
        self.y_move *= -1

    def Out_of_Boundary(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1


    # ball = Ball()

# scren.exitonclick()