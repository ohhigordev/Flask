# Primeiro importar o Flask e o render_template:
from flask import Flask, render_template

app = Flask(__name__)

# Vamos criar uma rota para a nossa pagina web
@app.route('/nomes')
def ListarNomes():

    lista = ['Higor', 'Nicole', 'Anna Laura']
    return render_template('lista_de_nomes.html',
                           titulo = 'Primeiro programa',
                           nomes = lista)

app.run(debug=True)


