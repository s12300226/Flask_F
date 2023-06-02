from flask import request, url_for, render_template, flash, session,redirect


from calcsalary import app


@app.route('/')
def show_entries():
    return render_template('index.html', default_input="")

@app.route('/test')
def show_tests():
    return render_template('test.html')

@app.route('/result', methods=['GET', 'POST'])
def show_result():

    # POSTされた値を取得
    if request.method=='POST':
        # バリデーションチェック
        # 空欄かチェック
        if request.form['salary'] == '':
            flash('給与が未入力です。入力してください')
            return redirect(url_for('show_entries'))
        
        # 入力上限(10桁以上だとダメ)
        if len(request.form['salary']) >= 10:
            flash('給与には最大9,999,999,999まで入力可能です')
            return render_template('index.html', default_input=request.form['salary'])
        
        if int(request.form['salary'])<0:
            flash('給与にはマイナスの値は入力できません')
            return render_template('index.html', default_input=request.form['salary'])

        input_salary = int(request.form['salary'])

        # 給与所得計算
        if input_salary > 100  * 10000:
            over_salary = input_salary - int(100 * 10000)
            tax_amount = int(100 * 10000 * 0.1 + over_salary * 0.2)
        else:
            tax_amount = int(input_salary * 0.1)
        payment = input_salary - tax_amount

        # カンマ区切りstr型で出力
        input_salary = "{:,}".format(input_salary)
        payment = "{:,}".format(payment)
        tax_amount = "{:,}".format(tax_amount)

        
    return render_template('result.html', result_salary=input_salary, result_payment=payment, result_tax = tax_amount)
