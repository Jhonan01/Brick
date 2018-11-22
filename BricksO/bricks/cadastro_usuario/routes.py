from flask import request, render_template, session
from peewee import *
from bricks.cadastro_usuario import cadastroUsuario_bp 
from werkzeug.security import generate_password_hash, check_password_hash
from bricks.models import Usuario, Itens

@cadastroUsuario_bp.route('/cadastro_usuario', methods=['GET', 'POST'])

def cadastro_usuario():

    return render_template('cadastro_usuario.html')



@cadastroUsuario_bp.route('/cadastro_enviado', methods = ['GET','POST'])
def cadastro_enviado():


    verificar = False
    c = request.form.get('email')
    for v in range(len(request.form.get('email'))):
        if(c[v] == '@'):
            verificar = True
            break

    if(verificar == False):
        return render_template('cadastro_usuario.html', error_cadastro = 'Email inválido')


    Usuario.create(usuario_login=request.form.get('usuario'), usuario_nome=request.form.get('nome'), usuario_senha=generate_password_hash(request.form.get('senha')), usuario_sobrenome=request.form.get('sobrenome'), usuario_email=request.form.get('email'), usuario_cidade=request.form.get('cidade'), usuario_estado=request.form.get('estado'))

    return """<html><head><title>Cadastro enviado</title></head>
             <body>
             <a href='/index'><h5>Início</h5></a> 
             </br>Cadastro realizado com sucesso!!!
             </body>
             </html>
             """
