from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/data/<table>')
def data(table):
    template = f'{table}.html'
    return render_template(template, table=table)


if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, render_template
# from flask_pymongo import pymongo

# app = Flask(__name__)

# CONNECTION_STRING = "mongodb+srv://isabely:cohorte8@cluster0.k2xgf.mongodb.net/apalabrados_dbretryWrites=true&w=majority"
# client = pymongo.MongoClient(CONNECTION_STRING)
# db = client.get_database('apalabrados_db')
# user_collection = pymongo.collection.Collection(db, 'user_collection')


# @app.route('/')
# def start():
#     db.NUMBERS.insert_one({'number': 999})
#     return render_template('index.html')


# @app.route('/data/<table>')
# def data(table):
#     return render_template('numbers.html', table=table)


# if __name__ == '__main__':
#     app.run(debug=True)    