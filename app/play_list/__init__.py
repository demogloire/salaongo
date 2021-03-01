from flask import Blueprint

play_list = Blueprint('play_list', __name__, url_prefix='/play_list')
# never forget 
from . import routes