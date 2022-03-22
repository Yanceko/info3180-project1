import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base Config Object"""
    DEBUG = False
    # Storage Location
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
    
    