from flask import Blueprint

download = Blueprint('download', __name__, url_prefix='/download')
# never forget 
from . import routes