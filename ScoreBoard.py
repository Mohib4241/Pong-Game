from turtle import  Turtle,Screen
#
# scr = Screen()
# scr.bgcolor("black")

align = 'center'
font =('Courier',80 ,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.penup()
        self.Update_Scoreboard()

    def Update_Scoreboard(self):
        self.clear()
        self.goto(x=-100,y=200)
        self.write(self.l_score ,align = align , font=font)
        self.goto(100,200)
        self.write(self.r_score ,align = align , font=font)


    def Update_Left_Score(self,L_score):
        self.l_score = L_score
        self.Update_Scoreboard()

    def Update_Right_Score(self, R_score):
        self.r_score = R_score
        self.Update_Scoreboard()