from flask import request, url_for, render_template, flash, session,redirect


from calcsalary import app


@app.route('/')
def show_entries():
    return render_template('index.html')

@app.route('/test')
def show_tests():
    return render_template('test.html')

@app.route('/result', methods=['GET', 'POST'])
def show_result():

    # POSTされた値を取得
    if request.method=='POST':

        if request.form['salary'] == '':
            print('空欄')
            flash('数字を入力してください')
            return redirect(url_for('show_entries'))

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
