from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.Role import Role
from datetime import datetime
from passlib.hash import pbkdf2_sha256

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=1, nullable=True)
    role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)

def get_user_by_email(self):
    """
    Construiremos essa fução
    """
    return ''

def get_user_by_id(self):
    """
    Construiremos essa fução
    """
    return ''

def update(self, obj):

    return ''

def hash_password(self, password):
    try:
        return pbkdf2_sha256.hash(password)
    except Exception as e:
        print ("Erro ao criptografar senha %s" % e)

def set_password(self, password):
    self.password = pbkdf2_sha256.hash(password)

def verify_password(self, password_no_hash, password_databse):
    try:
        return pbkdf2_sha256.verify(password_no_hash, password_databse)
    except ValueError:
        return False
