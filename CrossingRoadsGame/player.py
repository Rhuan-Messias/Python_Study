import turtle as t 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
        
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def next_level(self):
        self.goto(STARTING_POSITION)
        
        

