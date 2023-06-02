from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_entries():
    return render_template('input.html')


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
    # print('penguin')
    # 給与計算をする
    input_salary=int(request.form['salary'])
    # 出力チェック
    print(input_salary)
    print(type(input_salary))

    # 税額計算のため、給与1,000,000での判定
    if (input_salary > 1000000):
        tax = (input_salary - 1000000) * 0.2 + 100000
    else:
        tax = input_salary * 0.1

    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    # 支給額 = 給与 - 税額
    pay = input_salary - tax
    print('--------------')
    print(f'tax:{tax}')
    # 支給額の出力
    print("支給額:" + str(pay) + "、税額:" + str(tax), end="")

    return render_template('output.html', salary=input_salary, naka=pay, gawa=tax)
