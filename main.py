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


@app.route('/list_prof/<list>')
def list_prof(list):
    if list in ['ol', 'ul']:
        professions = ['Инженер', 'Ученый', 'Пилот', 'Медик', 'Биолог']
        return render_template('list_prof.html', list=list, professions=professions)
    else:
        return render_template('list_prof.html', list='error')


if __name__ == '__main__':
    app.run()
