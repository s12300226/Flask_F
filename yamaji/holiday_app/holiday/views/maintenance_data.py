from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Entry

@app.route('/maintenance_date', methods=['POST'])
def maintenance_date():

    if request.form['holiday'] == "" or request.form['holiday_text'] == "":
        flash("値を入力してください")
        return render_template('input.html')
    elif len(request.form['holiday_text']) > 20:
        flash("テキストは20文字以内で入力してください")
        return render_template('input.html')

    entry = Entry.query.get(request.form['holiday'])

    if request.form["button"] == "insert_date":
        if entry is None:
            entry = Entry(
                holi_date=request.form['holiday'],
                holi_text=request.form['holiday_text']
            )
            db.session.add(entry)
            db.session.commit()
            text = f"{request.form['holiday']}({request.form['holiday_text']})が登録されました"
            return render_template('result.html', text=text)
        else:
            entry.holi_date = request.form['holiday']
            entry.holi_text = request.form['holiday_text']
            db.session.merge(entry)
            db.session.commit()
            text = f"{request.form['holiday']}は{request.form['holiday_text']}に更新されました"
            return render_template('result.html', text=text)
    elif request.form["button"] == "delete":
        if entry is None:
            flash(f"{request.form['holiday']}は、祝日マスタに登録されていません")
            return render_template('input.html')
        else:
            db.session.delete(entry)
            db.session.commit()
            text = f"{request.form['holiday']}({request.form['holiday_text']})は、削除されました"
            return render_template('result.html', text=text)

    return render_template('input.html')