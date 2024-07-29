# Importando o flask para o projeto
from flask import Flask,render_template, request, redirect, session, flash, url_for

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

# Criando a classe de usuário:
class Usuario:
    def __init__(self,  nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

# Adicionando usuários a classe:
usuario01 = Usuario('Higor Freitas', 'Ohhigordev007', 'admin')
usuario02 = Usuario('Nicole Lima', 'Ahnicole1223', '1234')
usuario03 = Usuario('Pedro Jose', 'Pedrojose004', '1234567')


# Trablhando com dicionarios:
usuarios = {
    usuario01.login: usuario01,
    usuario02.login: usuario02,
    usuario03.login: usuario03
}


app = Flask(__name__)

app.secret_key = 'pindoretama'

@app.route('/')
def listarMusicas():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))



    return render_template('lista_musicas.html', 
                           titulo = 'Músicas Cadastradas',
                           musicas = lista)

@app.route('/cadastrar')
def cadastrar_musica():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))

    return render_template('cadastra_musica.html',
                           titulo = "Cadastrar Música")

@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['txtNome']
    cantorBanda = request.form['txtCantor']
    genero = request.form['txtGenero']

    novaMusica = Musica(nome, cantorBanda, genero)

    lista.append(novaMusica)
    return redirect(url_for('listarMusicas'))

# Criando a rota para a tela de login:
@app.route('/login')
def login():
    return render_template('login.html')

# Valindando o usuário:
@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if request.form['txtLogin'] in usuarios:

        usuarioEncontrado = usuarios[request.form['txtLogin']]

        if request.form['txtSenha'] == usuarioEncontrado.senha:

            # Aqui foi criada uma sessão apenas para um usuário em particular!
            session['usuario_logado'] = request.form['txtLogin']

            flash(f'Usuário {usuarioEncontrado.login} logado!')

            return redirect(url_for('listarMusicas'))
        
        else:
            flash('Senha inválida!')

            return redirect(url_for('login'))

    else:
        flash('Usuário ou senha invalida!')
        return redirect(url_for('login'))
    

@app.route('/sair')
def sair_sessao():
    session['usuario_logado'] = None # Sessão finalizada!

    return redirect('/login')


app.run(debug=True) 
