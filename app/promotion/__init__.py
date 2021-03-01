from flask import Blueprint

promotion = Blueprint('promotion', __name__, url_prefix='/promotion')
# never forget 
from . import routes