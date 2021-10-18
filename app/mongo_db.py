from flask import Flask, request, redirect, url_for
from flask_pymongo import pymongo
import pandas as pd

def mongodb():
    URL = "mongodb+srv://isabely:cohorte8@cluster0.k2xgf.mongodb.net/apalabrados_dbretryWrites=true&w=majority"
    client = pymongo.MongoClient(URL)
    db = client.get_database('apalabrados_db')
    return db

db = mongodb() 


def save_input():    
    input = request.form
    data = input['text']
    ascii_text = list(range(48, 58)) + list(range(65,91)) + list(range(97,123)) + [164,165]
    ord_values = [ord(i) for i in data]
    if data.isnumeric() == True:
        db.NUMBERS.insert_one({'Number': data})
        accumulate()
    elif [ord_values[i] for i in range(0, len(ord_values)) if ord_values[i] not in ascii_text]:
        data = ''.join([data[i] for i in range(0, len(data)) if ord_values[i] not in ascii_text])
        db.CHARACTERS.insert_one({'Character': data}) 
    else:
        db.TEXT.insert_one({'Text':data,'Initial':data[0],'Final':data[-1]})     
    return redirect(url_for('submit')) 


def accumulate():       
    current_id = db.NUMBERS.find().sort('_id', -1).limit(1)[0]['_id'];
    last_accumulated = db.NUMBERS.find().sort('_id', -1).limit(1)[1]['Accumulated'];
    current_number = db.NUMBERS.find().sort('_id', -1).limit(1)[0]['Number'];
    acummulated = int(last_accumulated) + int(current_number)
    db.NUMBERS.update({'_id':current_id},{'Number': current_number,'Accumulated':acummulated},upsert=True)


def tables():
    numbers_db = db.NUMBERS.find({},{'Number':1, 'Accumulated':1,'_id':0})
    df_num = pd.DataFrame.from_dict(numbers_db)
    num_data = df_num.to_html(index=False)

    text_db = db.TEXT.find({},{'Text':1,'Initial':1,'Final':1,'_id':0})
    df_text = pd.DataFrame.from_dict(text_db)
    text_data = df_text.to_html(index=False, justify='center',col_space='200px')

    char_db = db.CHARACTERS.find({},{'Character':1,'_id':0})
    df_char = pd.DataFrame.from_dict(char_db)
    char_data = df_char.to_html(index=False)

    tables = [num_data, text_data, char_data]

    return tables