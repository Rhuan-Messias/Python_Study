import turtle as t 

alignment = 'center'
chosen_font = ("Courier", 60, "normal")

class Score(t.Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.score_update() #call this function in the attributes in order to have the score since the start of the object
    
    def score_update(self):
        self.write(f"{self.score}",align=alignment, font=chosen_font)
       
    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_update()