from flasgger import Swagger
from flask import Flask

from app.extensions import db
from app.routes.short_urls import short_urls_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Encurtador de URLs',
        'doc_dir': './app/docs/'
    }
    app.config.from_object(Config)
    app.register_blueprint(short_urls_bp)

    swagger = Swagger(app=app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app