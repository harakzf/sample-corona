from flask import Blueprint, request, flash, url_for, redirect, render_template, session
from project.UserModel import User
from project.SettingPostgres import db_session
from sqlalchemy import *
from sqlalchemy.orm import *
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import hashlib

app = Blueprint('auth', __name__)

# 以下処理を記載したい
# ・ユーザ登録処理
# ・ログイン処理
# ・ログアウト処理


@app.route('/register', methods=('GET', 'POST'))
def register():
    '''
    ×登録処理
    〇ログイン処理
    '''
    hash = hashlib.sha256()

    if request.method == 'POST':

        # フォームからユーザ名とパスワードを取得(パスワードは暗号化して取得)
        username = request.form['username']
        password = request.form['password']

        # 必須チェック
        error = None
        if not username:
            error = 'ユーザ名を入力して下さい。'
        elif not password:
            error = 'パスワードを入力して下さい。'
        
        # パスワードを暗号化して取得
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # ユーザ情報をDB(PostgreSQL)から取得
        userInfo = db_session.query(User).filter(User.username == username).all()

        # メッセージ格納用変数定義
        error_msg = None

        # 認証チェック
        if len(userInfo) == 0 or userInfo[0].password != password_hash:
            error_msg = 'ユーザ名またはパスワードが間違っています。'

        # 認証成功した場合            
        if error_msg is None:
            
            # DBコミット
            db_session.commit()

            # ユーザセッションクリア
            session.clear()

            # ユーザセッション再作成
            session['user_id'] = userInfo[0].id

            flash('ログインに成功しました。')
            return redirect(url_for('show.show_entry'))

        # 認証成功していない(失敗した)場合の処理
        else:
            db_session.commit()
            flash(error_msg)

            return render_template('auth/auth_register.html')

        # db_session.add(User(username))
    
    # GETリクエストの場合
    return render_template('auth/auth_register.html')
        



        
    
    
