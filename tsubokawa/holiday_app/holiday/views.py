from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday.models.holidays import Holiday
from holiday import db

@app.route('/')
def home():
    return render_template('input.html')


@app.route('/list')
def show_holidays():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidays=holidays)

@app.route('/maintenance_date', methods=['POST'])
def delete_holiday():
    # 新規登録・更新ボタンが押されたときの処理
    if request.form['button'] == 'insert_update':
        # データ更新：DB上に同じ日付のデータがあるとき
        holiday = Holiday.query.get(request.form['holi_date'])
        if holiday != None:
        # 同じ日付のデータを上書き
            holiday.holi_text = request.form['holi_text']
            
            db.session.merge(holiday)
            db.session.commit()
            result_text = f'{holiday.holi_date}は「{holiday.holi_text}」に更新されました'
        
        else:
        # 新しくデータを登録
            holiday=Holiday(
                holi_date = request.form['holi_date'],
                holi_text = request.form['holi_text']
            )
            db.session.add(holiday)
            db.session.commit()
            result_text = f'{holiday.holi_date}({holiday.holi_text})が登録されました'

        # print(entry)
        return render_template('result.html', result_text=result_text)
    

    elif request.form['button'] == 'delete':
        holiday = Holiday.query.get(request.form['holi_date'])
        db.session.delete(holiday)
        db.session.commit()
        result_text = f'{holiday.holi_date}({holiday.holi_text})は削除されました'

        return render_template('result.html', result_text=result_text)
