# Importando o flask para o projeto
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/musicas')
def listarMusicas():

    lista = ['Lobo - Guará','Terror da Previdencia','Vai e Chora']


    return render_template('lista_musicas.html', 
                           titulo = 'Aprendendo do inicio com Daniel.',
                           musicas = lista)


app.run(debug=True) # Agora o que for feito de alteração sera atualiazado automaticamente.
