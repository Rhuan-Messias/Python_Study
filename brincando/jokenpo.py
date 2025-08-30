import random 
from IPython.display import clear_output
import os 

class Mao:
  def __init__(self):
    self.gesto = ''
  
  def set_gesto(self,gesto):
    self.gesto = gesto

  def get_gesto(self):
    return self.gesto


def point_increase(player):

  return 1

gestos = ['pedra', 'papel', 'tesoura']

minha_mao = Mao()
minha_mao_placar = 0
adversario_mao = Mao()
adversario_mao_placar = 0

keep = True
while (keep):
  print(f'Você {minha_mao_placar} X {adversario_mao_placar} Adversario')
  gesto = input('diga o gesto: ')
  minha_mao.set_gesto(gesto)

  adversario_mao.set_gesto(gestos[random.randint(0, len(gestos) - 1)])
  print(f"adversario: {adversario_mao.get_gesto()}")
  
  if minha_mao.get_gesto() == adversario_mao.get_gesto():
    print('empate')
  elif (minha_mao.get_gesto() == 'pedra' and adversario_mao.get_gesto() == 'papel'):
    print('você perdeu')
    adversario_mao_placar += 1
  elif(minha_mao.get_gesto() == 'pedra' and adversario_mao.get_gesto() == 'tesoura'):
    print('você venceu')
    minha_mao_placar += 1
  elif(minha_mao.get_gesto() == 'papel' and adversario_mao.get_gesto() == 'pedra'):
    print('você venceu')
    minha_mao_placar += 1
  elif(minha_mao.get_gesto() == 'papel' and adversario_mao.get_gesto() == 'tesoura'):
    print('voce perdeu')
    adversario_mao_placar += 1
  elif(minha_mao.get_gesto() == 'tesoura' and adversario_mao.get_gesto() == 'pedra'):
    print('voce perdeu')
    adversario_mao_placar += 1
  elif(minha_mao.get_gesto() == 'tesoura' and adversario_mao.get_gesto() == 'papel'):
    print('você venceu')
    minha_mao_placar += 1
  else: 
    print('Rodada Inválida')

  keep_going = input("")
  if keep_going == 'n':
    keep = False
  
  clear_output()
  os.system('clear')  


