from flask import Flask, render_template

app = Flask(__name__)

# Criar uma rota:
@app.route('/cadastrarMusica')
def Cadastro():
    return render_template('cadastra_musica.html')

app.run(debug=True)



