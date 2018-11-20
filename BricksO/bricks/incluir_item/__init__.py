from flask import Blueprint

incluirItem_bp = Blueprint('incluir_item',__name__)

from bricks.incluir_item import routes
