from flask import Blueprint

login_bp = Blueprint('login',__name__)

from bricks.login import routes 
