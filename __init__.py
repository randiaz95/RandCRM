from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = '9OLWxND2jh34h2H34h223g4wW4o83j4K4iuopO'

login_manager = LoginManager()
login_manager.login_view = 'index.index'
login_manager.init_app(app)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

csrf = CSRFProtect()
csrf.init_app(app)

import RandCRM.controllers.index
import RandCRM.controllers.login
