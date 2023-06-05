from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route('/')

def show_entries():
    return render_template('input.html')

@app.route('/', methods=['GET', 'POST'])
def input():
    input_data = session.get('input_data', None)
    return render_template("input.html", input = input_data)    

@app.route('/output', methods=['GET', 'POST'])
def output():
    session["input_data"] = ""
     
    if request.form["salary"] == "":
        flash('給与が未入力です。入力してください。')
        return redirect(url_for("input"))

    if int(request.form["salary"]) > 9999999999:
        flash('給与には最大9,999,999,999まで入力可能です。')
        session["input_data"] = request.form["salary"]
        return redirect(url_for("input"))

    if int(request.form["salary"]) < 0:
        flash('給与にはマイナスの値は入力できません。')
        session["input_data"] = request.form["salary"]
        return redirect(url_for("input")) 


    if request.method == "POST":
        input_salary = int(request.form["salary"])
        if (input_salary > 1000000):
            tax = (input_salary - 1000000) * 0.2 + 100000
        else:
            tax = input_salary * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        
        pay = input_salary - tax
    return render_template("output.html",  salary=input_salary, tax=tax, pay=pay)