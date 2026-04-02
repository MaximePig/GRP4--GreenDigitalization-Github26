from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

load_dotenv()

application = Flask(__name__)

### Code GitHub (les credentials sont dans le .env, pas dans le code)
application.config['SECRET_KEY'] = os.environ['SECRET_KEY']
DBVAR = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:5432/{os.environ['DB_NAME']}"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
application.config['SQLALCHEMY_BINDS'] = {'transport': DBVAR}


### Code computer
# application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'
# DBVAR = 'sqlite:///user.db'
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
# application.config['SQLALCHEMY_BINDS'] ={'transport': 'sqlite:///transport.db'}

# # application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
# application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
# # application.config['SQLALCHEMY_BINDS'] ={'transport': 'sqlite:///transport.db'}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

