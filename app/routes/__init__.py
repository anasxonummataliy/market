from flask import Flask

from .auth_route import auth_bp
from .main_route import main_bp
from .admin_route import admin_bp
from .category_route import category_bp


def register_all_blueprints(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(category_bp)
