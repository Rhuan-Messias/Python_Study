import turtle as t 

FONT = ("Courier", 20, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-215,240)
        self.score_update()
        
    def score_update(self):

        self.write(f'Level -> {self.score}', align='center', font= FONT)

    def score_increase(self):
        self.score += 1 
        self.clear()
        self.score_update()