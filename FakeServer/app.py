from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chave_secreta'

USUARIO_PADRAO = 'admin'
SENHA_PADRAO = 'senha123'
SENHAS = ['senha123', '123456', 'abc123', 'admin', 'password', 'qwerty', 'letmein', '12345678']

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == USUARIO_PADRAO and senha == SENHA_PADRAO:
        return redirect(url_for('sucesso'))
    else:
        return redirect(url_for('falha'))

@app.route('/sucesso')
def sucesso():
    return render_template('mensagem.html', mensagem='Login bem-sucedido!')

@app.route('/falha')
def falha():
    return render_template('mensagem.html', mensagem='Usuário ou senha incorretos!')

if __name__ == '__main__':
    app.run(debug=True)
