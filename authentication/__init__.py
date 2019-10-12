from flask import Blueprint

bp_auth = Blueprint('auth', __name__)    # oauth login routes
bp_login = Blueprint('login', __name__)  # front end login routes
bp_ologin = Blueprint('ownlogin', __name__)  # Our own login implementation routes
bp_oentity = Blueprint('ownentity', __name__)  # Our own login implementation routes
