from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from model.Role import Role
from model.User import User
from model.Category import Category
from model.Product import Product

def start_views(app, db):
    admin = Admin(app, name='Meu Estoque', template_mode='bootstrap3')
    