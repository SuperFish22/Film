from flask import Flask
#from flask_login import LoginManager
import os, config

#создали экземпляр приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('DevopConfig'))

#инцилизация расшерения
#login_maneger = LoginManager(app)
#login_maneger.login_view = 'login'


from . import views


