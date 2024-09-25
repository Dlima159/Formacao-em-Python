'''
velocidade_maxima = 100
multa_leve = 180
multa_grave = 550
multa_gravissima = 1500
'''
# CamelCase
class Radar:
  def __init__(self,velocidade_maxima,multa_leve,multa_grave,multa_gravissima):
    self.velocidade_maxima = velocidade_maxima
    self.multa_leve = multa_leve
    self.multa_grave = multa_grave
    self.multa_gravissima = multa_gravissima


radar1 = Radar(velocidade_maxima=100,multa_leve=180,multa_grave=550,multa_gravissima=1500)
print(radar1.velocidade_maxima)
print(radar1.multa_leve)
print(radar1.multa_grave)
print(radar1.multa_gravissima)

radar2 = Radar(velocidade_maxima=120,multa_leve=200,multa_grave=300,multa_gravissima=500)
print(radar2.velocidade_maxima)
print(radar2.multa_leve)
print(radar2.multa_grave)
print(radar2.multa_gravissima)