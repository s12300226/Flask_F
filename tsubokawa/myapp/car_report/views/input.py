from car_report import app
from flask import request, redirect, url_for, render_template, flash, session
import os
from datetime import datetime

new_filename = 'デフォルト'

@app.route('/')
def input():
    """
    入力画面へ遷移する処理
    """
    return render_template('input.html')

@app.route('/', methods=['POST'])
def output():
    """
    入力画面で入力値を取得して表示する処理
    """
    print(request.form['test_text'])
    file = request.files['image']
    # file.save(os.path.join('../../static/image', file.filename))
    # file.save(os.path.join('/home/matcha-23training/python/Flask/Flask_Frenchfries/tsubokawa/myapp/car_report/static/image', file.filename))
    global new_filename
    new_filename = app.config['USERNAME'] + str(datetime.utcnow())+'.jpg'
    # file.save(os.path.join('./car_report/static/image', file.filename))
    file.save(os.path.join('./car_report/static/image', new_filename))
    # print(f'ファイル名は{file.filename}です')
    print('#####################################')
    print(new_filename)
    return redirect(url_for('result'))

    # return render_template('input.html')

@app.route('/result')
def result():
    return render_template('result.html', new_filename=new_filename)