# Recursos: Listar, exibir, criar, alterar e excluir usuários
# Campos: id, name, cpf, email, phone_number, created_at, updated_at

from flask import Flask, render_template, request, redirect, session, flash, url_for


class Info:
    def __init__(self, id, name, cpf, email, phone, created, updated):
        self.id=id
        self.nome=name
        self.cpf=cpf
        self.email=email
        self.phone=phone
        self.created=created
        self.updated=updated

info1 = Info('1', 'João', '12345678900', 'joao@hotmail.com', '(14) 98888-8888', '21/05/2022', '20/02/2023')
info2 = Info('2', 'José', '12345678901', 'jose@hotmail.com', '(14) 98888-8889', '21/06/2022', '20/03/2023')
info3 = Info('3', 'Pedro', '12345678902', 'pedro@hotmail.com', '(14) 98888-8810', '21/07/2022', '20/04/2023')
list = [info1, info2, info3]

class Users:
    def __init__(self, nome, nickname, senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha

user1 = Users("Igor ALbuquerque", "VulgoRato", "123")
user2 = Users("Zé Zé", "zeze", "2105")
user3 = Users("João João", "JaoJao", "2050")
user4 = Users("Rafa Lima", "RafinhaRafa", "2002")
user5 = Users("Caio Café", "Cafe06", "0510")

usuarios = { user1.nickname : user1,
             user2.nickname : user2,
             user3.nickname : user3,
             user4.nickname : user4,
             user5.nickname : user5}


app = Flask(__name__)
app.secret_key = '21052002'


# Criando página inicial (Será a página home de quando estivermos logados - Trará os dados de: # Campos)
@app.route('/')
def index():
    return render_template('list.html', title='Users', users=list)

# Página de novos dados (A junção dessas duas páginas ("/novo" e "/criar") trará o input dos dados de: # Campos que seá mostrado em '/' = index = home)
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', title='Novo usuário')

# Até aqui OK

@app.route('/criar', methods=['POST',])
def criar():
     id = request.form['id']
     nome = request.form['nome']
     cpf = request.form['cpf']
     email = request.form['email']
     phone = request.form['phone']
     created = request.form['created']
     updated = request.form['updated']
     info = Info(id, nome, cpf, email, phone, created, updated)
     list.append(info)
     return redirect(url_for('index'))

# Página de validação de dados de acesso (Posso ver a possibilidade de retirar a página de login)
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

# Criando direção de autenticação de dados de acesso
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário ou senha inválidos!')
        return redirect(url_for('login'))

# Rota de Logout
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado.')
    return redirect(url_for('index'))
# Tentar criar um botão de Logout (Ver no projeto do CurriculoLandingPage e tentar usar a mesma tag semântica para criar o botão 'Logout' que direcione para o endereço '/')


# Criar uma rota que direcione para as páginas do arquivo orders.py
# Ou tentar criar tudo no mesmo arquivo


app.run(debug=True)