from flask import Blueprint


auth_bp = Blueprint("auth", __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
