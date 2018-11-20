from flask import Blueprint

lance_bp = Blueprint('lance',__name__)

from bricks.lance import routes
