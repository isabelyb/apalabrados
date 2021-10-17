from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import pymongo
import pandas as pd
from app import create_app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')

URL = "mongodb+srv://isabely:cohorte8@cluster0.k2xgf.mongodb.net/apalabrados_dbretryWrites=true&w=majority"
client = pymongo.MongoClient(URL)
db = client.get_database('apalabrados_db')

ndb = db.NUMBERS.find({},{'number':1, 'accumulated':1,'_id':0})
df = pd.DataFrame.from_dict(ndb)


num_data = df.to_html(index=False)


@app.route('/submit')
def submit():

    context = {
        'variable':'Mariu',
        'titles': ['Na','NUMBERS','TEXT','CHARACTER'],
        'tables': num_data
    }    
    return render_template('submit.html', **context)



ascii_text = list(range(48, 58)) + list(range(65,91)) + list(range(97,123)) + [164,165]

@app.route('/', methods=['POST'])
def save_input():
    input = request.form
    data = input['text']
    ord_values = [ord(i) for i in data]
    if data.isnumeric() == True:
        db.NUMBERS.insert_one({'number': data})
    elif [ord_values[i] for i in range(0, len(ord_values)) if ord_values[i] not in ascii_text]:
        data = ''.join([data[i] for i in range(0, len(data)) if ord_values[i] not in ascii_text])
        db.CHARACTERS.insert_one({'character': data}) 
    else:
        db.TEXT.insert_one({'character':data,'initial':data[0],'final':data[-1]})
    return redirect(url_for('submit')) 


@app.route('/data/numbers')
def accumulate():
    current_id = db.NUMBERS.find().sort('_id', -1).limit(1)[0]['_id'];
    last_accumulated = db.NUMBERS.find().sort('_id', -1).limit(1)[1]['accumulated'];
    current_number = db.NUMBERS.find().sort('_id', -1).limit(1)[0]['number'];
    acummulated = int(last_accumulated) + int(current_number)
    db.NUMBERS.update({'_id':current_id},{'number': current_number,'accumulated':acummulated},upsert=True)
    return render_template('numbers.html')



if __name__ == '__main__':
    app.run(debug=True)

