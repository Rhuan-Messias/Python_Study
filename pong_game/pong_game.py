import turtle
import paddle
import ball
import time
import score

right_paddle = paddle.Paddle(350,0)
left_paddle = paddle.Paddle(-350,0)
little_ball = ball.Ball()
left_score = score.Score((-50,220))
right_score = score.Score((50,220))

screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor('Black')
screen.title('***** PONG GAME *****')
screen.tracer(0) #turn off the animation, but makes necessary manually update the screen


#to make the paddles go up and down 
screen.listen()
screen.onkey(right_paddle.up,"i")
screen.onkey(right_paddle.down,'k')
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,'s')

game_is_working = True 
speed = 0.005

while game_is_working:
    time.sleep(speed)
    screen.update()
    little_ball.movement()    
    # collision with upper or down 
    if little_ball.ycor() == 300 or little_ball.ycor() == -300:
        little_ball.collision_wall()
    elif little_ball.xcor() > 338 and little_ball.distance(right_paddle) <50 or little_ball.xcor() < -338 and little_ball.distance(left_paddle)<50:
        little_ball.collision_paddle()
        if speed > 0.0018:
            speed -= 0.00005
        else:
            pass
    elif little_ball.xcor()>380:
        left_score.score_increase()
        speed = 0.004
        little_ball.reset()
    elif little_ball.xcor()<-380:
        right_score.score_increase()
        speed = 0.004
        little_ball.reset()  
    else:
        pass
    
    # collision with paddles

    
    

screen.exitonclick()
