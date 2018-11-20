from flask import request, render_template, session
from bricks.lance import lance_bp
from bricks.models import Usuario, Itens, Imagens, Lances, db 


@lance_bp.route("/lances/", methods = ['GET', 'POST'])

def lances():

    user = Usuario.get(Usuario.usuario_login == session['usuario'])
    
    if(request.args.get('id_user_lancador')):        
        Lances.create(lances_id_user_lancador_id=request.args.get('id_user_lancador'), lances_id_user_alvo=request.args.get('id_user_alvo'), lances_id_item_lancador_id=request.args.get('id_item_lancador'), lances_id_item_alvo=request.args.get('id_item_alvo'))

    tudo = []   
    def getDados(controle):
        lances = []
        if (controle == 'lancador'):
            query_meus_lances =  Lances.select().where(Lances.lances_id_user_lancador_id == user.id)
        else:
            query_meus_lances =  Lances.select().where(Lances.lances_id_user_alvo == user.id)            
        

        for data in query_meus_lances:
            
            dados_item_lancador = Itens.get(Itens.id == data.lances_id_item_lancador)
            item_lancador_img = Imagens.get(Imagens.imagens_id_itens_id == dados_item_lancador.id)
            dados_item_alvo = Itens.get(Itens.id == data.lances_id_item_alvo)
            item_alvo_img =Imagens.get(Imagens.imagens_id_itens_id == dados_item_alvo.id)
            
            a={            
                "lances_id_user_lancador": data.lances_id_user_lancador_id,
                'lances_user_img_lancador': item_lancador_img.imagens_name_hash,
                'lance_user_titulo_lancador': dados_item_lancador.itens_titulo,
                'lance_user_desc_lancador':  dados_item_lancador.itens_descricao ,

                'lances_id_user_alvo': data.lances_id_user_alvo,
                'lances_user_img_alvo': item_alvo_img.imagens_name_hash,
                'lance_user_titulo_alvo': dados_item_alvo.itens_titulo,
                'lance_user_desc_alvo':  dados_item_alvo.itens_descricao        
            }
            lances.append(a)

        return lances        
    

    
    tudo.append(getDados('lancador'))
    
    tudo.append(getDados('alvo'))
    
    

    return render_template('lance.html', lances = tudo)


@lance_bp.route("/aceitar/", methods = ['GET', 'POST'])

def aceitar():
    
    return request.form.get('aceitar')

@lance_bp.route("/recusar/", methods = ['GET', 'POST'])
def recusar():

    return request.form.get('recusar')

