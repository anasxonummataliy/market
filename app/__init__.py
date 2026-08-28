from flask import Flask

from app.core.config import conf
from app.models import db, migrate, bcrypt, login_manager
from app.routes import register_all_blueprints

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=conf.secret_key,
        WTF_CSRF_SECRET_KEY=conf.wtf_scrf_secret_key,
        SQLALCHEMY_DATABASE_URI=conf.db_uri,
    )

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    register_all_blueprints(app)

    return app
