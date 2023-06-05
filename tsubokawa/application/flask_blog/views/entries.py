from flask import request, url_for, render_template, flash, session,redirect

from flask_blog import app

from flask_blog import db

from flask_blog.models.entries import Entry



@app.route('/')
def show_entries():
    # ログインしていないとlogin.htmlにリダイレクト
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # templates/entries/index.htmlを返す設定
    entries = Entry.query.order_by(Entry.id.desc()).all()


    return render_template('entries/index.html', entries=entries)



"""
記事を作成するメソッド
"""
@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    # 作成時は、db.session.add(作成対象)
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))



"""

"""
@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')



"""
「続きを読む」リンクを押したときの遷移処理
"""

@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)





"""
更新ボタンを押すと、更新ページに遷移するメソッド
"""
@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)



"""
記事を更新するメソッド
"""
@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']

    # 更新の時は、db.session.merge(更新する対象)
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))


"""
記事を削除するメソッド
"""

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))
