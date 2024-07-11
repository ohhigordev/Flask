# Importando o flask para o projeto
from flask import Flask

app = Flask(__name__)

# Criando a rota da nossa aplicação:
@app.route('/inicio')
def hello():
    return '<h1>Bem vindo a minha primeira aplicação flask</h1>' # Imprimindo um titulo


app.run()
