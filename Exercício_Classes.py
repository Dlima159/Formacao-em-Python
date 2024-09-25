
class Artista:
    def __init__(self,nome_do_artista,genero_de_musica,albuns):
        self.nome_do_artista = nome_do_artista
        self.genero_de_musica = genero_de_musica
        self.albuns = albuns
    
    def adicionar_albuns(self,nome_album):
        self.albuns+= nome_album

    def listar_albuns(self):
        for album in self.albuns:
            print(f'O artista {self.nome_do_artista} do gênero musical {self.genero_de_musica} possui o seguinte album:{album}')

artista1 = Artista('Metallica','Heavy Metal',['Black Album'])
artista1.adicionar_albuns(['St. Anger','Kill\'em All'])
artista1.listar_albuns()
artista1.adicionar_albuns(['And Justice for All...'])
artista1.listar_albuns()
artista2 = Artista('Linkin Park','NuMetal',['Hybrid Theory'])
artista2.adicionar_albuns(['Meteora', 'Minutes to Midnight'])
artista2.listar_albuns()