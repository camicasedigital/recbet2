import os

class Config:
    url = os.getenv('DATABASE_URL')
    if not url:
        raise RuntimeError("❌ DATABASE_URL não está configurada no ambiente.")
    
    SQLALCHEMY_DATABASE_URI = url.replace("mysql://", "mysql+pymysql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
