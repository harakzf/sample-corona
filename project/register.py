from flask import Blueprint, request, flash, redirect, url_for, render_template
from dateutil.parser import parse
import project
import datetime

app = Blueprint('register', __name__)

@app.route('/add', methods=['POST'])
def add_entry():
    '''
    登録処理を実装するモジュール
    '''

    # 登録フォーム(name)の内容をそれぞれ変数に格納
    billName = request.form['bills']
    workingDay = parse(request.form['workingDay'])
    temperature = request.form['temperature']

    # mongoDB接続用API呼び出し
    mongo = project.db_config()

    # mongoDBに登録
    mongo.db.base.insert_one({"billName": billName, "workingDay": workingDay, "temperature": temperature})

    # 登録完了後にフラッシュメッセージ生成
    flash('登録が正常に完了しました！')

    # 登録TOP画面にリダイレクト
    return redirect(url_for('show.show_entry'))

