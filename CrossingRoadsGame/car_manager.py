import turtle as t 
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1000


class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.goto(300,random.randint(-250,300))
        self.setheading(180)
    
    def car_movement(self):
        self.forward(self.speed)
    
    def next_level_speed(self):
        self.speed += MOVE_INCREMENT
        self.car_movement()
        


        
