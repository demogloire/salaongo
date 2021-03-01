from flask import Blueprint

categorieMusique = Blueprint('categorieMusique', __name__, url_prefix='/categorieMusique')
# never forget 
from . import routes