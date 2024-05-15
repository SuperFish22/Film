import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    SEKRET_KEY = os.environ.get("")
    bd_name = "C:/Users/Fish/Desktop/Новая папка (3)/tutorial.db"

class DevopConfig(BaseConfig):
    debag = True

class TestConfig(BaseConfig):
    debag = True

class ProductConfig(BaseConfig):
    debag = False