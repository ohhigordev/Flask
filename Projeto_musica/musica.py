# Importando o flask para o projeto
from flask import Flask,render_template, request, redirect

# Vamos criar uma classe em python:
class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero): # Aqui definimos os parametros!!!
        self.nome = nome # Isso aqui são os atributos.
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero

musica01 = Musica('Temporal','Hungria', 'Hip-Hop')
musica02 = Musica('Papai Banca','MC Ryan SP', 'Funk')
musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03]



app = Flask(__name__)

@app.route('/')
def listarMusicas():


    return render_template('lista_musicas.html', 
                           titulo = 'Aprendendo do inicio com Daniel.',
                           musicas = lista)

@app.route('/cadastrar')
def cadastrar_musica():
    return render_template('cadastra_musica.html')

@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['txtNome']
    cantorBanda = request.form['txtCantor']
    genero = request.form['txtGenero']

    novaMusica = Musica(nome, cantorBanda, genero)

    lista.append(novaMusica)
    return redirect('/')


app.run(debug=True) # Agora o que for feito de alteração sera atualiazado automaticamente.
