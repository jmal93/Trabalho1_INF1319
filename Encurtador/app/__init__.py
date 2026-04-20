from flask import Flask
from app.extensions import db, swagger
from app.routes.short_urls import short_urls_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    swagger.init_app(app)

    app.register_blueprint(short_urls_bp)

    with app.app_context():
        db.create_all()

    return app