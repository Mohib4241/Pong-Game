from time import sleep
from turtle import Turtle,Screen


# scReen = Screen()
# scReen.tracer(0)
# # # scReen.bgcolor("black")

class Paddle(Turtle):

    def __init__(self,x,y,shape="square",color="white"):
        super().__init__()
        # self.hideturtle()
        self.shape(shape)
        self.color(color)
        self.turtlesize(5,1)
        self.penup()
        # self.speed("fastest")
        self.goto(x=x,y=y)
        # self.showturtle()


    def move_upward(self):
        if self.pos()[1] < 380:
            self.goto(self.position()[0],self.pos()[1]+20)


    def move_downward(self):
        if self.pos()[1] > -380:
            self.goto(self.position()[0],self.pos()[1]-20)




# Paddl = Paddle()
# Paddl.move_upward()
# Paddl.move_downward()
# scReen.exitonclick()
