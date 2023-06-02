from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_tsubo():
    return "ツボだよ"


if __name__ == '__main__':
    app.run()
