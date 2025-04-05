from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_dance.contrib.google import make_google_blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    from .routes import bp as main_bp
    from .auth import bp as auth_bp
    from .webhook import bp as webhook_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(webhook_bp, url_prefix="/webhook")

    google_bp = make_google_blueprint(
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        redirect_url="/login/google/authorized",
        scope=["profile", "email"]
    )
    app.register_blueprint(google_bp, url_prefix="/login")

    from .models import Cliente, Corrida, RoteiroTuristico
    admin = Admin(app, name='Painel Executivo', template_mode='bootstrap3')
    admin.add_view(ModelView(Cliente, db.session))
    admin.add_view(ModelView(Corrida, db.session))
    admin.add_view(ModelView(RoteiroTuristico, db.session))

    with app.app_context():
        db.create_all()

    return app
