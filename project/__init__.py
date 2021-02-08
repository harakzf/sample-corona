from flask import Flask
from flask_pymongo import PyMongo
from project import show, register, auth

app = Flask(__name__)
app.secret_key = 'secret'

# 実行ファイル(モジュール)の分割設定
app.register_blueprint(show.app)
app.register_blueprint(register.app)
app.register_blueprint(auth.app)

# mongoDBの設定メソッド
def db_config():
    # mongoDBサーバ設定（ローカル用）
    app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/kawamuradb'
    mongo = PyMongo(app)

    return mongo

