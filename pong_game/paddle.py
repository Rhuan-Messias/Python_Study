
import turtle

paddle_movement = 20
up_angle = 90
down_angle = 270


class Paddle(turtle.Turtle):
    
    def __init__(self,x,y):
        super().__init__()
        self.objects_list =[]
        self.create_paddle(x,y)
        self.paddle = self.objects_list[0]
        

    def create_paddle(self,x_cor,y_cor):
        self.shape('square')
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x_cor,y_cor)
        self.objects_list.append(self)

    def up(self):
        self.paddle.goto(self.paddle.xcor(),self.paddle.ycor()+20)
    def down(self):
        self.paddle.goto(self.paddle.xcor(),self.paddle.ycor()-20)
