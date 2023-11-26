import turtle as t 


alignment = 'center'
chosen_font = ("Arial", 24, "normal")

class Ball(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.penup()
        self.color('white')
        self.x_move = 1
        self.y_move = 1

    def movement(self):
       x_increase = self.xcor() + self.x_move
       y_increase = self.ycor() + self.y_move
       self.goto(x_increase,y_increase)
       
    def collision_wall(self):
        self.y_move *= -1   #using this method to change the direction of y movement

    def collision_paddle(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.collision_paddle()
        
       
        

    def fim(self):
        self.goto(0,0)
        self.write("---> Game Over <---",align=alignment, font = chosen_font)
