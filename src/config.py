class Config(object):
    SECRET_KEY='password'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/dongalleto'
    SQLALCHEMY_TRACK_MODIFICATIONS = False