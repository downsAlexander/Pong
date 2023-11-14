from turtle import Screen
import time
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle1, Paddle2

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle1 = Paddle1((350, 0))
paddle2 = Paddle2((-350, 0))
ball = Ball()
l_score = ScoreBoard((-50, 250))
r_score = ScoreBoard((50, 250))

screen.listen()
screen.onkey(fun=paddle1.go_up, key="Up")
screen.onkey(fun=paddle1.go_down, key="Down")
screen.onkey(fun=paddle2.go_up, key="w")
screen.onkey(fun=paddle2.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle1) < 50 and ball.xcor() >= 330:
        ball.rally()

    if ball.distance(paddle2) < 50 and ball.xcor() <= -330:
        ball.rally()

    if ball.xcor() > 380:
        l_score.add_point()
        ball.ball_reset()
    elif ball.xcor() < -380:
        r_score.add_point()
        ball.ball_reset()








screen.exitonclick()