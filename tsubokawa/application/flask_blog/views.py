"""
/にリクエストがあった時の処理


URLにアクセスがあった時の処理
@app.route(URL)
def xxx():
    処理

"""
from flask import request, url_for, render_template, flash, session,redirect

from flask_blog import app

@app.route('/')
def show_entries():
    # templates/entries/index.htmlを返す設定
    return render_template('entries/index.html')

@app.route('/test')
def show_tests():
    # templates/entries/index.htmlを返す設定
    return render_template('entries/test.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME']:
            print('ユーザー名が違うよ')
        elif request.form['password']!= app.config['PASSWORD']:
            print('パスワードが違うよ')
        else:
            return redirect('/')
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    return redirect('/')