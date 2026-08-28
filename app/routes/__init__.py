from flask import Flask

from .auth_route import auth_bp
from .main_route import main_bp


def register_all_blueprints(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
