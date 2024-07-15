# Importando o flask para o projeto
from flask import Flask,render_template

# Vamos criar uma classe em python:
class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero): # Aqui definimos os parametros!!!
        self.nome = nome # Isso aqui são os atributos.
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero




app = Flask(__name__)

@app.route('/musicas')
def listarMusicas():

    musica01 = Musica('Temporal','Hungria', 'Hip-Hop')
    musica02 = Musica('Papai Banca','MC Ryan SP', 'Funk')
    musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')

    lista = [musica01, musica02, musica03]


    return render_template('lista_musicas.html', 
                           titulo = 'Aprendendo do inicio com Daniel.',
                           musicas = lista)


app.run(debug=True) # Agora o que for feito de alteração sera atualiazado automaticamente.
