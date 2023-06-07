from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Entry

# DBの追加、更新、削除結果を表示するページ
@app.route('/maintenance_date', methods=['POST'])
def maintenance_date():

    holiday = request.form['holiday']
    holiday_text = request.form['holiday_text']

    # バリデーション
    if validate(holiday,holiday_text):
        return render_template('input.html')

    # 入力された日付をDBで検索
    entry = Entry.query.get(holiday)

    # 追加または更新の場合の処理
    if request.form["button"] == "insert_date":
        if entry is None:
            edit_entry(holiday, holiday_text)
            text = f"{holiday}({holiday_text})が登録されました"
            return render_template('result.html', text=text)
        else:
            update_entry(holiday, holiday_text)
            text = f"{holiday}は{holiday_text}に更新されました"
            return render_template('result.html', text=text)
    # 削除の場合の処理
    elif request.form["button"] == "delete":
        if entry is None:
            flash(f"{holiday}は、祝日マスタに登録されていません")
            return render_template('input.html')
        else:
            delete_entry(holiday)
            text = f"{holiday}({holiday_text})は、削除されました"
            return render_template('result.html', text=text)

    return render_template('input.html')


# バリデーション処理まとめ
def validate(holiday, holiday_text):
    if holiday == "" or holiday_text == "":
        flash("値を入力してください")
        return True
    elif len(holiday_text) > 20:
        flash("テキストは20文字以内で入力してください")
        return True
    return False


# DBに新規登録する処理
def edit_entry(holiday, holiday_text):
    entry = Entry(
        holi_date=holiday,
        holi_text=holiday_text
        )
    db.session.add(entry)
    db.session.commit()
    return


# DBを更新する処理
def update_entry(holiday, holiday_text):
    entry = Entry.query.get(holiday)
    entry.holi_date = holiday
    entry.holi_text = holiday_text
    db.session.merge(entry)
    db.session.commit()
    return


# DBを削除する処理
def delete_entry(holiday):
    entry = Entry.query.get(holiday)
    db.session.delete(entry)
    db.session.commit()
    return