"""
/にリクエストがあった時の処理


URLにアクセスがあった時の処理
@app.route(URL)
def xxx():
    処理

"""
from flask import request, url_for, render_template, flash, session,redirect

from flask_blog import app

# Userクラスをインポートして、ログインユーザーの管理に使用
from flask_blog.models.login import User

from functools import wraps

from flask import Blueprint

view = Blueprint('view', __name__)

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner



@view.route('/test')
def show_tests():
    # templates/entries/index.htmlを返す設定
    return render_template('entries/test.html')

@view.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':

        #####ユーザー情報からログイン処理#########################
        users = User.query.order_by(User.id.desc()).all()
        for user in users:
            if request.form['username'] == user.username and request.form['password']==user.password:
                session['logged_in'] = True
                flash('ログインしました')
                # ホームへ移動
                return redirect(url_for('entry.show_entries'))
        
        flash('ユーザ名かパスワードが違います')
    return render_template('login.html')


        ###############################


    #     # username = request.form['username']
    #     if request.form['username']!=app.config['USERNAME']:
    #         flash('ユーザー名がちがうよ！')
    #     elif request.form['password']!= app.config['PASSWORD']:
    #         flash('パスワードが違うよ！')
    #     else:
    #         # ログイン成功したらログイン状態に設定
    #         # user_name = request.form['username']
    #         # print(user_name)
    #         session['logged_in'] = True
    #         flash('ログインしました')
    #         # ホームへ移動
    #         return redirect(url_for('show_entries'))
    # print('-------------------------')
    # return render_template('login.html')
    
@view.route('/logout')
def logout():
    """
    ログアウト処理
    """
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))

# 存在しないURLにアクセスしたときはログイン画面に遷移
# @view.app_errorhandler(404)
@view.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('view.login'))