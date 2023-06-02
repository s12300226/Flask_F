from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route('/')
def show_entries():
    return render_template("./input.html")

@app.route('/input_value', methods=['GET', 'POST'])
def input_value():
    if request.method:
        # バリデーション
        if request.form['salary'] == "":
            flash("給与が未入力です。")
            return redirect(url_for('show_entries'))
        
        input_salary = int(request.form['salary'])
        if input_salary > 9999999999:
            flash("給与には最大9,999,999,999まで入力可能です。")
            return redirect(url_for('show_entries'))
        elif input_salary < 0:
            flash("給与にマイナスの値は入力できません。")
            return redirect(url_for('show_entries'))
        
        # 給与計算
        payment_amount, tax_amount = calc_salary(input_salary)
        return render_template("./output.html", salary = input_salary, payment = payment_amount, tax = tax_amount)
    
    return redirect(url_for('show_entries'))

@app.route('/out_result', methods=['GET', 'POST'])
def out_result():
    return redirect(url_for('show_entries'))

# 給与計算を行う関数
def calc_salary(salary):
    # 税率の変わる境界の値段
    border_tax = 1000000
    # 境界以下の場合の税率
    per_tax_l = 0.1
    # 境界より多い場合の税率
    per_tax_h = 0.2


    if salary <= border_tax:
        tax_amount = salary * per_tax_l
    else:
        tax_amount = (salary - border_tax) * per_tax_h + border_tax * per_tax_l

    # 税率の四捨五入
    tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding="ROUND_HALF_UP")
    payment_amount = salary - tax_amount

    return payment_amount, tax_amount