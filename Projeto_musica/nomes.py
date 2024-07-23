# Primeiro importar o Flask e o render_template:
from flask import Flask, render_template, request, session, redirect

# Vamos criar uma classe em python:
class Name:
    def __init__(self, nome, sobrenome, sexualidade): # Aqui foi criado os parametros
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexualidade = sexualidade # Aqui definimos os nossos atributos!

nome1 = Name('Higor', 'Freitas', 'M')
nome2 = Name('Nicole', 'Lima', 'F')
nome3 = Name('Anna Laura', 'Freitas', 'F')

lista = [nome1, nome2, nome3]

app = Flask(__name__)

app.secret_key = 'pindoretama'

# Vamos criar uma rota para a nossa pagina web
@app.route('/')
def ListarNomes():

    
    return render_template('lista_de_nomes.html',
                           titulo = 'Primeiro programa',
                           nomes = lista)


@app.route('/cadastrarNomes')
def Cadastar():
    return render_template('cadastrar_nomes.html')


# Cadastar nomes novos:
@app.route('/adicionar', methods =['POST',])
def adiconar_nomes():
    nome = request.form['txtPrimeiroNome']
    sobrenome = request.form['txtSobrenome']
    genero = request.form['txtGenero']

    Novonome = Name(nome, sobrenome, genero)


    lista.append(Novonome)
    return render_template('lista_de_nomes.html',
                           titulo = 'Primeiro Lista de nomes',
                           nomes = lista)


# Criando rota para a tela de login:
@app.route('/loginNomes')
def tela_login():
    return render_template('login_nomes.html')

# Validando usuário:
@app.route('/autenticar', methods = ['POST',])
def autenticar_nomes():
    if request.form['txtSenha'] == 'admin':
        # Aqui foi criada uma sessão em particular para o usuário:
        session['usuário_logado'] = request.form['txtLogin']
        return redirect('/') # Redirecionar para a página inicial
    
    else:
        return redirect('/loginNomes')

@app.route('/sair')
def sair_sessao():
    session['usuario_logado'] = None # Sessão finalizada

    return redirect('/')

            

app.run(debug=True)

