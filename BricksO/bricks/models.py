from peewee import *
from bricks import db

class Usuario(Model):
    usuario_login = CharField()
    usuario_nome = CharField()
    usuario_senha = CharField()
    usuario_email = CharField()
    usuario_cidade = CharField()
    usuario_estado = CharField()

    class Meta:
        database = db

class Itens(Model): 
    itens_titulo = CharField() 
    itens_descricao = CharField()
    itens_categoria = CharField()
    itens_id_users = ForeignKeyField(Usuario) 
 
    class Meta: 
        database = db 

class Imagens(Model):
    imagens_name_hash = CharField()
    imagens_id_itens = ForeignKeyField(Itens)


    class Meta:
        database = db

class Lances(Model):
    lances_id_user_lancador = ForeignKeyField(Usuario)
    lances_id_item_lancador = ForeignKeyField(Itens)
    lances_id_user_alvo = IntegerField()    
    lances_id_item_alvo = IntegerField()

    class Meta:
        database = db

try:
    Lances.create_table()
    print("Tabela 'Lances' criada com sucesso")

except OperationalError:
    print("Tabela 'Lances' Já existe")


try:
    Usuario.create_table()
    print("Tabela 'Usuario' criada com sucesso")

except OperationalError:
    print("Tabela 'Usuario' Já existe")

try:
    Itens.create_table()
    print("Tabela criada 'Itens' com sucesso")

except OperationalError:
    print("Tabela 'itens' já existe")
    
try:
    Imagens.create_table()
    print("Tabela 'Imagens' criada com sucesso")

except OperationalError:
    print("Tabela 'Imagens' já existe")

