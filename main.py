from flask import Flask, render_template
import re

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title='Страница подготовки к миссии на Марс'):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

if __name__ == '__main__':
    app.run()
