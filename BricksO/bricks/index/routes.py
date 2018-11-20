from flask import request, render_template, session
from bricks.index import index_bp
from flask import Flask, url_for
from bricks.models import Usuario, Itens, Imagens, db, Lances
from werkzeug.security import generate_password_hash, check_password_hash

@index_bp.route('/index', methods = ['GET', 'POST'])

def index():

    if request.method == 'POST':
    
        query = Usuario.select(Usuario.usuario_login).where(Usuario.usuario_login == request.form.get('usuario')).get()
        
        #queryS = Usuario.select(Usuario.usuario_senha).where(Usuario.usuario_senha == request.form.get('senha')).get()



        if('{0.usuario_login}'.format(query) == request.form.get('usuario')):

            session['usuario'] = request.form.get('usuario')
            usuario_local = request.form.get('usuario')
            return render_template('index.html', logado='Você está logado') 

    return render_template('index.html', logado='Você não está logado')



@index_bp.route('/pesquisa', methods = ['GET', 'POST'])

def pesquisa():
   
    if request.method == 'POST':

        procuraTitulo = Itens.select().where(Itens.itens_categoria == request.form.get('pesquisa'))
        d=[]
        for iten in procuraTitulo:
            imagens = Imagens.select().where(Imagens.imagens_id_itens_id == iten.id)
            img=[]            
            j=0
            for imagen in imagens:
               img.insert(j,imagen.imagens_name_hash)
               j+= 1
            e = {
                  
                  'id': iten.id,
                  'id_user': iten.itens_id_users_id,
                  'titulo': iten.itens_titulo,
                  'descricao': iten.itens_descricao,
                  'imagens': img
                } 
            d.append(e)
                   
        quantiO = len(d)

        return render_template('pesquisa.html', resultadoTitulo=d, quantidadeObjetos = quantiO)

    return render_template('index.html')


@index_bp.route('/carregar_oferta/', methods = ['GET', 'POST'])

def carregar_oferta():
    
    queryU = Usuario.get(Usuario.usuario_login == session['usuario'])

    selecionarItens = Itens.select().where(Itens.itens_id_users_id == queryU.id)
    
    s=[]
    for a in selecionarItens:
        

        selecionarImagens = Imagens.select().where(Imagens.imagens_id_itens_id == a.id)
        imagem=[]
        t=0
        for teste in selecionarImagens:
            imagem.insert(t, teste.imagens_name_hash)
            t+=1
        b = {
                
                'id': a.id,
                'id_user_lancador': a.itens_id_users_id, 
                'id_user_alvo': request.args.get('id_user_alvo'),
                'id_item_alvo': request.args.get('id_item_alvo'),
                'titulo': a.itens_titulo,
                'descricao': a.itens_descricao,
                'imagens': imagem
                
                }    
        s.append(b)

    print(s)

    return render_template('carregar_oferta.html',si = s)


