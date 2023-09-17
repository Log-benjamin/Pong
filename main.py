from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Collision with Paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 350 or ball.distance(l_paddle) < 30 and ball.xcor() < -350:
        ball.bounce_x()

    #Detect Right Padddle Miss
    if ball.xcor() > 380:
        ball.reset_poisition()
        scoreboard.l_point()
    
    #Detect Left Paddle Miss
    if ball.xcor() < -380:
        ball.reset_poisition()
        scoreboard.r_point()

screen.exitonclick()