from flask import Flask, render_template
from app import create_app
from app.mongo_db import mongodb, accumulate, save_input, tables


app = create_app()
db = mongodb()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def data():
    return save_input()


@app.route('/submit')
def submit():    
    context = {
        'variable':'Mariu',
        'titles': ['NUMBERS','TEXT','CHARACTER'],
        'tables': tables()
    }    
    return render_template('submit.html', **context)
    

if __name__ == '__main__':
    app.run(debug=True)

