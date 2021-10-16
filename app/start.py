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

######## Get from mongo ####

@app.route('/data/numbers')
def last_id():
    current_id = db.NUMBERS.find().sort('_id', -1).limit(1)[0]['_id'];
    last_number = db.NUMBERS.find().sort('_id', -1).limit(1)[1]["number"];
    current_number = db.NUMBERS.find().sort('_id', -1).limit(1)[0]["number"];
    acummulated = int(last_number) + int(current_number)
    print(acummulated)
    db.NUMBERS.update({'_id':current_id},{'number': current_number,'accumulated':acummulated},upsert=True)
    return render_template('numbers.html')


############################

@app.route('/data/submit')
def submit():    
    return render_template('submit.html')


@app.route('/data/<table>')
def data(table):
    template = f'{table}.html'
    return render_template(template, table=table)


if __name__ == '__main__':
    app.run(debug=True)

