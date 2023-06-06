from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday.models.holidays import Holiday
from holiday import db

@app.route('/')
def home():
    """
    祝日の入力画面に戻る処理
    """
    return render_template('input.html')


@app.route('/list')
def show_holidays():
    """
    祝日のリストを表示する処理
    """
    # holidaysにはDB内の全ての祝日のデータが入っている
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidays=holidays)

@app.route('/maintenance_date', methods=['POST'])
def delete_holiday():
    """
    祝日が入力されたときの処理（登録・更新・削除はifで処理）
    """

    # 新規登録・更新ボタンが押されたときの処理
    if request.form['button'] == 'insert_update':
        # データ更新：DB上に同じ日付のデータがあるとき
        # 同じ日付のデータを取得
        holiday = Holiday.query.get(request.form['holiday'])
        if holiday != None:

        # 更新処理
            holiday.holi_text = request.form['holiday_text']
            
            db.session.merge(holiday)
            db.session.commit()
            result_text = f'{holiday.holi_date}は「{holiday.holi_text}」に更新されました'
        
        else:

        # 新規登録処理
            holiday=Holiday(
                holi_date = request.form['holiday'],
                holi_text = request.form['holiday_text']
            )
            db.session.add(holiday)
            db.session.commit()
            result_text = f'{holiday.holi_date}({holiday.holi_text})が登録されました'

        return render_template('result.html', result_text=result_text)
    


    # 削除ボタンが押されたときの処理
    elif request.form['button'] == 'delete':
        holiday = Holiday.query.get(request.form['holiday'])
        db.session.delete(holiday)
        db.session.commit()
        result_text = f'{holiday.holi_date}({holiday.holi_text})は削除されました'

        return render_template('result.html', result_text=result_text)
