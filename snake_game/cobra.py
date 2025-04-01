import turtle as t

# lembre-se que em python, uma constante é nomeada com todas as letras
# maiúsculas
POSIÇÃO_INICIAL = [(0,0),(-20,0),(-40,0)]
RASTEJAR = 20
CIMA = 90
BAIXO = 270
DIREITA = 0
ESQUERDA = 180 

#classe começa com letra maiúscula 
# Toda vez que crio uma cobra dessa classe, aparecerá as 3 partes do
# corpo, e se moverá da maneira correta 
class Cobrinha:

    def __init__(self):
        self.partes_do_corpo = []
        self.criar_cobrinha()
        self.cabeça = self.partes_do_corpo[0]
    
    def criar_cobrinha(self):
        for i in POSIÇÃO_INICIAL:
            self.crescer(i) #usa a função crescer, para crescer os 3 primeiros quadrados

       
    
    def crescer(self, position):
        #aumenta um quadradinho na cobrinha 
        cobrinha = t.Turtle(shape='square')
        cobrinha.color('gray10')
        cobrinha.penup()
        cobrinha.goto(position)
        self.partes_do_corpo.append(cobrinha)
    
    def engordar(self):
        self.crescer(self.partes_do_corpo[-1].position())

        
    #esse pedaço de código vai fazer com que a cobrinha se mova para
    #frente automaticamente
    def mover(self):
        for parte in range(len(self.partes_do_corpo)-1,0,-1):
            posição_x = self.partes_do_corpo[parte-1].xcor()
            posição_y = self.partes_do_corpo[parte-1].ycor()
            self.partes_do_corpo[parte].goto(posição_x,posição_y)
        self.cabeça.forward(RASTEJAR)

    def cima(self):
        if self.cabeça.heading() != BAIXO:
            self.cabeça.setheading(CIMA)
    def baixo(self):
        if self.cabeça.heading() != CIMA:
            self.cabeça.setheading(BAIXO)
    def esquerda(self):
        if self.cabeça.heading() != DIREITA:
            self.cabeça.setheading(ESQUERDA)
    def direita(self):
        if self.cabeça.heading() != ESQUERDA:
            self.cabeça.setheading(DIREITA)