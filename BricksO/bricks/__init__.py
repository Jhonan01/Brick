from flask import Flask 
from bricks.config import Config
from peewee import *



db = SqliteDatabase('dados.db')




def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  

  from bricks.lance import lance_bp
  app.register_blueprint(lance_bp)
  
  from bricks.login import login_bp
  app.register_blueprint(login_bp)

  from bricks.cadastro_usuario import cadastroUsuario_bp
  app.register_blueprint(cadastroUsuario_bp)
  
  from bricks.index import index_bp
  app.register_blueprint(index_bp)

  from bricks.incluir_item import incluirItem_bp
  app.register_blueprint(incluirItem_bp)



  return app




