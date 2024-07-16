# Primeiro importar o Flask e o render_template:
from flask import Flask, render_template, request

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

# Vamos criar uma rota para a nossa pagina web
@app.route('/nomes')
def ListarNomes():

    
    return render_template('lista_de_nomes.html',
                           titulo = 'Primeiro programa',
                           nomes = lista)


@app.route('/cadastrarNomes')
def Cadastar():
    return render_template('cadastrar_nomes.html')


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
            

app.run(debug=True)


