from flask import request, url_for, render_template, flash, session,redirect


from calcsalary import app

@app.route('/')
def show_entries():
    return render_template('index.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    print('計算中')
    # return render_template('result.html')
    return redirect(url_for('show_result'))

@app.route('/result')
def show_result():
    return render_template('result.html')