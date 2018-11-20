from bricks.incluir_item import incluirItem_bp
from flask import request, render_template, session
from werkzeug.utils import secure_filename
import os
from peewee import *
from bricks.models import Itens, Usuario, Imagens
from werkzeug.security import generate_password_hash, check_password_hash
import base64

UPLOAD_FOLDER = './bricks/static/img/itens'


@incluirItem_bp.route('/incluir_item', methods = ['GET', 'POST'])
def incluir_item():

    return render_template('incluir_item.html')




@incluirItem_bp.route('/enviado', methods = ['GET', 'POST'])
def enviado():

    if request.method == 'POST':

        f = request.files['imagem']
        filename = secure_filename(f.filename)
        newName = base64.b64encode(filename.rsplit('.',1)[0].encode())
        newName = newName+'.'.encode()+filename.rsplit('.', 1)[1].encode()
        f.save(os.path.join(UPLOAD_FOLDER,newName.decode()))
        


        query = Usuario.get(Usuario.usuario_login == session['usuario'])


        Itens.create(itens_titulo=request.form.get('name'), itens_descricao=request.form.get('descricao'), itens_categoria=request.form.get('categoria'), itens_id_users=query)

        queryI = Itens.get(Itens.itens_titulo == request.form.get('name'))

        Imagens.create(imagens_name_hash=newName, imagens_id_itens=queryI)

        return render_template('index.html')
