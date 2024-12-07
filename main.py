from time import sleep
from turtle import  Turtle,Screen
from Paddle import Paddle
from Ball import Ball
from  ScoreBoard import  ScoreBoard
from Screen_Setup import  Screen_Setup

screen = Screen()
# height = 600
# width = 800
# screen.setup(height=height,width=width)
screen.tracer(0)





User_Paddle = Paddle(-350,0)
Another_User_Paddle = Paddle(350,0)
ball = Ball()
ScoreBoard = ScoreBoard()
setup = Screen_Setup()

screen.listen()



game = True
right_score = 0
left_score = 0
ball_speed = 0.01
while game:
    ball.start()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_with_wall()

    # Detect Collision with r_paddle
    if ball.distance(Another_User_Paddle) < 50 and ball.xcor() > 325 :
        print("right Contact made")
        ball.collision_with_X_bounce()
        ball_speed += 0.01


    elif ball.distance(User_Paddle) < 50 and ball.xcor() < -325 :
        print("left contact made")
        ball.collision_with_X_bounce()
        ball_speed += 0.01


    #Scores
    if ball.xcor() < -380:
        # Right gain score
        ball_speed = 0
        ball.Out_of_Boundary()
        right_score += 1
        ScoreBoard.Update_Right_Score(right_score)


    if ball.xcor() > 380:
        # Left Gain score
        ball_speed = 0
        ball.Out_of_Boundary()
        left_score += 1
        ScoreBoard.Update_Left_Score(left_score)


    if( ball_speed   == 0.1):
        game = False
        break

    # print(right_score)
    # print(left_score)
    sleep(0.1 - ball_speed)
    screen.update()


    screen.onkeypress(fun=User_Paddle.move_upward, key="w")
    screen.onkeypress(fun=User_Paddle.move_downward, key="s")
    screen.onkeypress(fun=Another_User_Paddle.move_upward, key="Up")
    screen.onkeypress(fun=Another_User_Paddle.move_downward, key="Down")

screen.exitonclick()