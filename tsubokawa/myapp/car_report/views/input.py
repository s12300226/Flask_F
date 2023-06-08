from car_report import app
from flask import request, redirect, url_for, render_template, flash, session
import os
from datetime import datetime
from car_report import db
from car_report.models.reports import Report
from car_report.models.reports_mst import Mst_Report

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
    print(request.form['text'])
    file = request.files['image']
    # file.save(os.path.join('../../static/image', file.filename))
    # file.save(os.path.join('/home/matcha-23training/python/Flask/Flask_Frenchfries/tsubokawa/myapp/car_report/static/image', file.filename))
    global new_filename
    new_filename = app.config['USERNAME'] + str(datetime.now())+'.jpg'
    # file.save(os.path.join('./car_report/static/image', file.filename))
    file.save(os.path.join('./car_report/static/image', new_filename))
    # print(f'ファイル名は{file.filename}です')
    print('#####################################')
    print(new_filename)
    return redirect(url_for('result'))

    # return render_template('input.html')

@app.route('/add_report', methods=['POST'])
def add_report():
    """
    画像、位置情報などをDBに登録する処理
    """
    # ファイル名を’ユーザー名’+'現在時刻'.jpgにする
    file = request.files['image']
    global new_filename
    new_filename = app.config['USERNAME'] + str(datetime.now())+'.jpg'

    # ファイルをstatic/imageフォルダに保存
    file.save(os.path.join('./car_report/static/image', new_filename))

    # ファイル名とユーザー名を登録
    report = Report(
        username = app.config['USERNAME'],
        file_name = new_filename,
        text = request.form['text']
    )

    db.session.add(report)
    db.session.commit()
    return redirect(url_for('input'))

@app.route('/show_reports')

def show_reports():
    """
    データを一覧表示する処理
    """
    # reports = Report.query.order_by(Report.report_date.asc()).all()
    # statusが未対応のデータのみ表示
    reports = db.session.query(Report).filter(Report.status=='未対応').order_by(Report.report_date.asc()).all()
    return render_template('image_output.html', reports=reports)

@app.route('/change_status', methods=['POST'])
def change_status():
    """
    statusを対応済みに変更する処理
    """
    print(request.form['change_button']) # idが出力されるはず
    report_id = request.form['change_button']
    report = db.session.query(Report).filter(Report.id==report_id).first()
    report.status = '対応済み'
    db.session.merge(report)
    db.session.commit()
    flash('対応済みに変更しました')
    return redirect(url_for('show_reports'))


@app.route('/mst_login', methods=['GET', 'POST'])
def mst_login():
    """
    Get時はマスターログイン画面に遷移する処理
    Post:入力された値が管理者かどうかのチェック
    管理者の場合、result.htmlへ遷移
    """
    if request.method=='POST':
        mst_reports = Mst_Report.query.order_by(Mst_Report.mst_id.asc()).all()
        for mst_report in mst_reports:
            if request.form['mst_name'] == mst_report.mst_name\
            and request.form['mst_pass'] == mst_report.mst_pass:
                session['logged_in'] = True
                flash('管理者としてログインしました')
                # result.hemlに遷移
                return redirect(url_for('show_reports'))
        flash('ユーザー名かパスワードが違います')
    return render_template('mst_login.html')
            

    # return render_template('mst_login.html')

@app.route('/logout')
def logout():
    """
    ログアウト処理
    """
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('input'))


@app.route('/result')
def result():
    return render_template('result.html', new_filename=new_filename)