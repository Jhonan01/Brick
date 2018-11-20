from flask import Blueprint

cadastroUsuario_bp = Blueprint('cadastro_usuario',__name__)

from bricks.cadastro_usuario import routes
