"""
/にリクエストがあった時の処理


URLにアクセスがあった時の処理
@app.route(URL)
def xxx():
    処理

"""


from flask_blog import app

@app.route('/')
def show_entries():
    return "Hello The World!"