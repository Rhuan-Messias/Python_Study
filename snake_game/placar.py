from turtle import Turtle

alinhamento = "center"
fonte = ("Arial", 24, "normal")

class Placar(Turtle): #isso é a classe hereditária de turtle
    def __init__(self): #aqui podemos por os atributos e métodos da classe
        super().__init__()
        self.placar = 0
        self.color("Black")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.atualizar_placar()
    
    def atualizar_placar(self):
        self.write(f"Placar: {self.placar}",align=alinhamento, font=fonte)
    
    def aumentar_placar(self): #isso é função
        self.placar += 1
        self.clear()
        self.atualizar_placar()
    
    def fim(self):
        self.goto(0,0)
        self.write('Você Perdeu !', align = alinhamento, font = fonte)
        