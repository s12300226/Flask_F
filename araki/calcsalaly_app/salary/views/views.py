from flask import request, redirect, url_for, render_template,flash,session #必要なもののインポート
from salary import app #
from decimal import Decimal, ROUND_HALF_UP

@app.route('/',methods=['GET','POST'])
def calc_start():
    return render_template('input.html')

@app.route('/calc',methods=['GET','POST'])
def calc():
    price_num = str(request.form['salaly_num'])
    if(price_num == ""):
        flash('給与が未入力です。入力してください。')
        return render_template('input.html')
    price_num = int(request.form['salaly_num'])
    if(price_num < 0):
        flash('給与はマイナスの値は入力できません。')
    elif(price_num >= 1000000000):
        flash('給与には最大9,999,999,999まで入力可能です。')
    else:
        if price_num > 1000000:
            tax_num = (price_num - 1000000) / 5
            tax_num = tax_num + 100000
        #100万以下の場合
        else:
            tax_num = price_num / 10
        tax_num = Decimal(tax_num).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        return render_template('output.html', price = price_num, tax = tax_num)
    return render_template('input.html')
