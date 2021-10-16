from flask import Flask, render_template, request
from flask_pymongo import pymongo
from app import create_app
from flask import redirect, url_for


app = create_app()


@app.route('/')
def start():
    return render_template('index.html')


URL = "mongodb+srv://isabely:cohorte8@cluster0.k2xgf.mongodb.net/apalabrados_dbretryWrites=true&w=majority"
client = pymongo.MongoClient(URL)
db = client.get_database('apalabrados_db')

@app.route('/', methods=['POST'])
def save_input():
    input = request.form
    data = input['text']
    db.NUMBERS.insert_one({'number': data})
    return redirect(url_for('submit')) 


@app.route('/data/submit')
def submit():    
    return render_template('submit.html')


@app.route('/data/<table>')
def data(table):
    template = f'{table}.html'
    return render_template(template, table=table)



if __name__ == '__main__':
    app.run(debug=True)

