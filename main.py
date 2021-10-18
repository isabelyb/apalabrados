from flask import Flask, render_template
from mongo_db import mongodb, accumulate, save_input, tables


app = Flask(__name__)
db = mongodb()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def data():
    return save_input()


@app.route('/submit', methods=['GET'])
def submit():    
    context = {
        'titles': ['NUMBERS','TEXT','CHARACTER'],
        'tables': tables()
    }    
    return render_template('submit.html', **context)
    

if __name__ == '__main__':
    app.run(debug=True)