from holiday import app
from flask import request, redirect, url_for, render_template, flash
from holiday.models.mst_holiday import Entry
from holiday import db


@app.route('/maintenance_date', methods=['POST'])
def change_holiday():  #20文字以上の場合
    if len(request.form['holiday_text'])> 20:
        flash("文字数は20文字以内で入力してください")
        return redirect(url_for('show_entries'))

    elif request.form['holiday'] == "":  #日付が空欄の場合
        flash('日付を再度入力してください。')
        return redirect(url_for('show_entries'))
    
    elif request.form['button'] == 'insert_update':
        if request.form['holiday_text'] == '': #holiday_textが空欄の場合
            flash('祝日名を入力してください。')
            return redirect(url_for('show_entries'))
        holiday = Entry.query.get(request.form['holiday'])

        if holiday != None:  #既にデータがある場合
            holiday.holi_text = request.form['holiday_text']        
            db.session.merge(holiday)
            db.session.commit()
            result_text = f'{holiday.holidate}は「{holiday.holi_text}」に更新されました'
        
        else:  #データがない場合
            holiday=Entry(
                holidate = request.form['holiday'],
                holi_text = request.form['holiday_text']
            )
            db.session.add(holiday)
            db.session.commit()
            result_text = f'{holiday.holidate}({holiday.holi_text})が登録されました'
    
    elif request.form['button'] == 'delete':
        holiday = Entry.query.get(request.form['holiday'])
        if holiday == None:
            flash(f"{request.form['holiday']}は、祝日マスタに登録されていません")
            return redirect(url_for('show_entries'))

        else:
            db.session.delete(holiday)
            db.session.commit()
            result_text = f'{holiday.holidate}({holiday.holi_text})は削除されました'

    return render_template('result.html', result_text=result_text)
