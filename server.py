from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER = "admin"
PASSWORD = "senhadoadmin"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == USER and senha == PASSWORD:
            return "Login bem-sucedido!"
        else:
            return render_template('index.html', error="Credenciais inválidas")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)