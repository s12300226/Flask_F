from flask import request, url_for, render_template, flash, session,redirect


from calcsalary import app

salary = 0
input_salary, tax_amount, payment = 10,0,0

@app.route('/')
def show_entries():
    return render_template('index.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    print('計算中')
    # POSTされた値を取得
    if request.method=='POST':
        print(request.form['salary'])
        input_salary = int(request.form['salary'])
        # 給与所得計算
        if input_salary > 100  * 10000:
            over_salary = input_salary - int(100 * 10000)
            tax_amount = int(100 * 10000 * 0.1 + over_salary * 0.2)
        else:
            tax_amount = int(input_salary * 0.1)
        payment = input_salary - tax_amount
        print(input_salary)

        
    # return render_template('result.html', result_salary=input_salary, result_payment=payment, result_tax = tax_amount)
    return redirect(url_for('show_result'))

@app.route('/result')
def show_result():
    return render_template('result.html', result_salary=input_salary, result_payment=payment, result_tax = tax_amount)
    # return render_template('result.html')