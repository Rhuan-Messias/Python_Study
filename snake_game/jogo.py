import turtle as t 
import cobra as c
import time
from comida import Comida
from placar import Placar

tela = t.Screen()
tela.setup(width=600, height=600) #keyword arguments, quando o parâmetro recebe as informações, onde azul é o parametro e a o numero é o argumento chave
tela.bgcolor('green')
tela.title('Jogo da Cobrinha')
tela.tracer(0)

cobrinha = c.Cobrinha() #vai rodar o __init__, criando a cobrinha com 3 segmentos
comida = Comida()
placar = Placar()


tela.listen()
#precisa ser em inglês, para indicar que são as setinhas 
tela.onkey(cobrinha.cima,"Up")
tela.onkey(cobrinha.baixo,"Down")
tela.onkey(cobrinha.esquerda,"Left")
tela.onkey(cobrinha.direita,"Right")


jogo_rodando = True 
while jogo_rodando:
    tela.update()
    time.sleep(0.1)
    cobrinha.mover() #chamamos o método movimento 

    #detectar colisão com a comidinha
    if cobrinha.cabeça .distance(comida) < 15:
        comida.refresh()
        cobrinha.engordar()
        placar.aumentar_placar() 

    #detectar colisão com a parede
    if cobrinha.cabeça.xcor() >300 or cobrinha.cabeça.xcor() < -300 or cobrinha.cabeça.ycor() > 300 or cobrinha.cabeça.ycor() < -300:
        jogo_rodando = False
        placar.fim()





tela.exitonclick()