from flask import Blueprint

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    return "Página de login"

@bp.route('/logout')
def logout():
    return "Logout realizado"
