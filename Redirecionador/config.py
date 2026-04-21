from os import environ


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") or 'sqlite:///urls.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False