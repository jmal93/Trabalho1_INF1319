from flask import Flask

from app.extensions import db, swagger
from app.routes.redirect_urls import redirect_url_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    swagger.init_app(app)
    
    app.register_blueprint(redirect_url_bp)
        
    return app