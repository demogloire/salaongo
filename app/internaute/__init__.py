from flask import Blueprint

internaute = Blueprint('internaute', __name__, url_prefix='/internaute')
# never forget 
from . import routes