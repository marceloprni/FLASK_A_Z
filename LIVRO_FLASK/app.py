from flask import Flask, request
#CONFIG IMPORT
from config import app_config, app_active
config = app_config[app_active]

#LINHA SQL
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello World'
    
    @app.route('/login/')
    def login():
        return 'Aqui entrar a tela de login'

    @app.route('/recovery-password/')
    def recovery_password():
        return 'Aqui entrar a tela de recuperar senha'
    
    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id, action):
        if action == 'action1':
            return 'Ação action1 usuario de ID %d' % id
        elif action == 'action2':
            return 'Ação action2 usuario de ID %d' % id 
        elif action == 'action3':
            return 'Ação action3 usuario de ID %d' % id
    
    @app.route('/profile', methods=['POST'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']

        return 'Essa rota possui um metodo POST e criará um usuario com os dados de usuario %s e senha %s' % (username, password)
    
    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']

        return 'Essa rota possui um metodo PUT e editará o nome do usuário para %s e a senha para %s' % (username, password)

    return app