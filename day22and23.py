from turtle import  Turtle,Screen
from pong import Pong # type: ignore
from ball import Ball # type: ignore
import time
from score import Score # type: ignore
screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle=Pong((-350,0))
l_paddle=Pong((350,0))
ball=Ball()
score=Score()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"u")
screen.onkey(l_paddle.go_down,"d")
game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        score.l_board()

    if ball.xcor()<-380:
        ball.reset_position()
        score.r_board()






screen.exitonclick()