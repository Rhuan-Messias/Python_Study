#pip install pygame
from os import MFD_ALLOW_SEALING
#NoneType quer dizer que não tem nada dentro da variavel

import pygame
import os
import random
import neat

ai_jogando = True
geracao = 0

TELA_LARGURA = 500
TELA_ALTURA = 800

#Como as imagens são pequenas, vamos usar a scale para dobrar o tamanho

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
IMAGENS_PASSARO = [
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))
]

#para decidir a fonte é preciso iniciar e escolher
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial',30)


class Passaro:
    IMGS = IMAGENS_PASSARO

    # animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        #Calcular o deslocamento
        self.tempo += 1

        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        #Restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
        #Angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # definir qual imagem do passaro usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
        # se o passaro estiver caindo, não animar as asas

        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2 # ajuste para a batida de asa ser para baixo
        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem,self.angulo)
        pos_centro_imagem = self.imagem.get_rect( topleft = ( self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center = pos_centro_imagem)
        tela.blit(imagem_rotacionada,retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):

        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50,450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):

        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        #para ver se houve colisão
        topo_ponto = passaro_mask.overlap(topo_mask,distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask,distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        #precisa criar dois chãos para um entrar qnd o outro sair da tela
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 += self.LARGURA*2
        if self.x2 + self.LARGURA < 0:
            self.x2 += self.LARGURA*2

    def desenhar(self,tela):
        tela.blit(self.IMAGEM,(self.x1,self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND,(0,0))

    for passaro in passaros:
        passaro.desenhar(tela)

    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255,255,255))
    tela.blit(texto,(TELA_LARGURA - 10 - texto.get_width(),10))

    if ai_jogando:
        texto = FONTE_PONTOS.render(f"Geração: {geracao}", 1, (255, 255, 255))
        tela.blit(texto, (10, 10))

    chao.desenhar(tela)

    pygame.display.update()

def main(genomas, config): #fitness function (quao bem um passaro foi) -> obrigatoriamente recebe genomas e config
    global geracao
    geracao += 1 # cada vez que a IA executa a main, é uma geração

    if ai_jogando:
        # o genoma é como a rede neural se modifica
        redes = [] # que corresponde a primeira rede dessa
        lista_genomas = [] # corresponde ao primeiro genoma dessa ^
        passaros = [] # primeiro passaro dessa ^

        for _, genoma in genomas: # como é uma lista de tupla (idGenoma, Genoma) coloca-se _ para dizer que não está em uso
            rede = neat.nn.FeedForwardNetwork.create(genoma,config)
            redes.append(rede)
            genoma.fitness = 0 # dar punicoes por más acoes e recompensas por boas acoes, ela busca acoes que aumentam esse fitness
            lista_genomas.append(genoma)
            passaros.append(Passaro(230,350))
    else:
        passaros = [Passaro(230,350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA)) # cria a tela
    pontos = 0
    relogio = pygame.time.Clock() # taxa de atualização

    rodando = True
    while rodando:
        relogio.tick(30) # fps

        #interação do usuário
        for evento in pygame.event.get(): #verificar clicks
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if not ai_jogando:
                if evento.type == pygame.KEYDOWN: #evento de apertar uma tecla
                    if evento.key == pygame.K_SPACE:
                        for passaro in passaros:
                            passaro.pular()

        indice_cano = 0
        if len(passaros) > 0:
            # descobrir qual cano olhar
            if len(canos) > 1 and passaros[0].x > (canos[0].x + canos[0].CANO_TOPO.get_width()):
                indice_cano = 1
        else:
            rodando = False
            break
        #mover os objetos
        for i,passaro in enumerate(passaros):
            passaro.mover()
            if ai_jogando:
                #aumentar um pouco a fitness
                lista_genomas[i].fitness += 0.1
                #output vai ficar entre -1 e 1, se for maior 0.5 pula
                output = redes[i].activate((passaro.y,
                                            abs(passaro.y - canos[indice_cano].altura),
                                            abs(passaro.y - canos[indice_cano].pos_base)))
                if output[0] > 0.5:
                    passaro.pular()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros): # assim pega-se o index do passaro na lista
                if cano.colidir(passaro):
                    passaros.pop(i) #remove o passaro da lista
                    if ai_jogando:
                        lista_genomas[i].fitness -= 1
                        lista_genomas.pop(i)
                        redes.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()

            if cano.x + cano.CANO_BASE.get_width() < 0 :
                remover_canos.append(cano)

            #não adicionar ou remover canos enquanto percorre a lista para não dar problema

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
            if ai_jogando:
                for genoma in lista_genomas:
                    genoma.fitness += 5
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if(passaro.y < 0 or passaro.y + passaro.imagem.get_height() > chao.y):
                passaros.pop(i)
                if ai_jogando:
                    lista_genomas.pop(i)
                    redes.pop(i)
        desenhar_tela( tela, passaros, canos, chao, pontos)


def rodar(caminho_config):
    # puxar as configuracoes da IA
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                caminho_config)
    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())

    if ai_jogando:
        populacao.run(main,50) #passa a fitness function e quantas vezes rodar se quiser
    else:
        main(None,None)
if __name__ == '__main__':
    caminho_config = 'config.txt'
    rodar(caminho_config)

