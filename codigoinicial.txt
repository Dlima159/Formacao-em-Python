velocidade_maxima = 100
multa_leve = 180
multa_grave = 550
multa_gravissima = 1500

def calcular_multa(velocidade,velocidade_maxima):
  if velocidade <= velocidade_maxima:
      print('Nao levou multa')

  elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
      print('Levou multa leve')

  elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
      print('Levou multa grave')

  elif velocidade > velocidade_maxima + 20:
      print('Levou multa gravissima')


def aplicar_penalizacao_carteira(nivel_multa):
  if nivel_multa == 'Multa leve':
    print('Perdeu 3 pontos na carteira')
    
  elif nivel_multa == 'Multa grave':
    print('Perdeu 5 pontos na carteira')
    
  else:
    print('Perdeu 7 pontos na carteira')


'''
velocidade_maxima = 100
multa_leve = 180
multa_grave = 550
multa_gravissima = 1500
'''
# CamelCase
class Radar:
  def __init__(self):
    self.velocidade_maxima = 80


radar1 = Radar()
print(radar1.velocidade_maxima)
