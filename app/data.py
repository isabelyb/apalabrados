from flask import Flask
from flask_pymongo import pymongo
from start import app



CONNECTION_STRING = "mongodb+srv://isabely:cohorte8@cluster0.k2xgf.mongodb.net/apalabrados_dbretryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('apalabrados_db')
user_collection = pymongo.collection.Collection(db, 'user_collection')













# from pymongo import MongoClient
# import requests

# client = MongoClient('mongodb+srv://isabely:cohorte8@cluster0.k2xgf.mongodb.net/apalabrados_dbretryWrites=true&w=majority')

# db = client.get_database('apalabrados_db')

# input_user = requests.get('web app apalabrados')
# input_user = input_user.json()

# NUMBERS = db.get_collection('input_user')



 




# from flask_pymongo import PyMongo
# from flask import Flask

# app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/apalabrados_db"
# mongodb_client = PyMongo(app)
# db = mongodb_client.db


# @app.route("/save")
# def save():
#     db.NUMBERS.insert_one({'number': 'input', 'accumulated':'input_sum'})
#     return flask.jsonify(message="success")



# @app.route("/")
# def home():
#     number_table = db.NUMBERS.find()
#     return flask.jsonify(['Table'])

