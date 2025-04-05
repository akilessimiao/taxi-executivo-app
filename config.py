import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-super-secreta')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///executivo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'chave-jwt-padrao')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
