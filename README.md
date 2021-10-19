# Apalabrados

**Apalabrados** is a nice database to save the user input and store it according to the data type.
* **Numbers:** It saves your input and accumulates with the last accumulated.
* **Text:** It saves your input and its first and last character.
* **Special characters:** It saves it from your input, only the special characters.

**Apalabrados** is part of challenge of diagnostic in Platzi Master Cohort[8].

## How to use it

**Step 1:** go to [Home](https://apalabrados-isabely.herokuapp.com/) and insert and input you want.

![home](/assets/home.jpg)

**Step 2:** When you have submitted an input **Apalabrados** redirect to app [response](https://apalabrados-isabely.herokuapp.com/submit).
There you can see the result of database that is saved and proceced yhe input according to the data type. 

![submit](/assets/submit.jpg)

You could go to back to the home and try the times you want!

## How to I made it

To develop this app I followed this steps in its order.

1. Made a github [repository](https://github.com/isabelyb/apalabrados).
2. Made a first version of the process with data flowchart. Then I have to adjust some details i nthe develop app process. I use [drawio](https://app.diagrams.net/) to do it.
    ![data_process](/assets/apalabrados_flowchart.drawio.svg)
3. How I feel more comfortable with Python, I looked for a better way to do a Web App using it. I found the more efficient tool was Flask, so I learned from zero how to do it.
I read a lot of sources, these were the most helpful for me:
    * [Platzi](https://platzi.com/clases/flask/)
    * [Documentation](https://palletsprojects.com/p/flask/)
    * [Pythonise tutorial](https://pythonise.com/series/learning-flask/flask-application-structure)
    * [python-adv-web-apps](https://python-adv-web-apps.readthedocs.io/en/latest/flask.html)
4. Made a first version of the App structure. As the _proces data flowchart_ I have to adjust some details in the develop app process. Too, I use [drawio](https://app.diagrams.net/) to do it.
    ![app_structure](/assets/app.drawio.svg)
5. Looked for learning about how to connect MongoDB with a Flask App. Some time ago I have learned about some basics from mongo in [Platzi](https://platzi.com/clases/mongodb/).
    [Mongodb](https://docs.mongodb.com/)
    [Pythonbasics tutorial](https://pythonbasics.org/flask-mongodb/)
6. Code! _By the way, my computer runs Ubuntu 20.04._
    6.1. Create a virtual environment: ```virtualenv venv``` -> ```source venv/bin/activate```
    6.2. Install Flask: ```pip3 install Flask```
    6.3. Create file main.py in order to start my web app.
    6.4. Config environment variables from the command line.
        ```export FLASK_APP=main.py``` -> Define to run Web App from main.py
        ```export FLASK_DEBUG=1```     -> Turn the debugger on to follow the Web App development.
    6.5. Run Flask to try the Web App: ```flask run```
    6.6. Saved requirements.txt. Update every tool installation: ```pip3 freeze > requirements.txt```
    6.7. Create database in mongodb:
        [mongo_db](/assets/mongo_db.jpg)
    6.8. Install Flask-PyMongo and conect database with the Web App:

    6.9. Create a Python code to manage data from the user Input with mongo. I used pandas too, to do it.
        * create clasifier function
                * make to input is saved in mongodb (without classifier)
        * get data from mongo db
        * accumulated numbers
    * post acumulated in accumulated column !!
    * post all data in the collection of bd in mongo
    * Updated get table in html from mongo db
    * modules
    * format html


## Deploy in [HEROKU](https://www.heroku.com/)



Cli


gunicorn: procfile

runtime: Version Python

My Web App was deployed and I felt so happy for this. 
This is my first App complet from zero to deploy.

Finally i finish to write the README.md file.

[View **Apalabrados** deployment here](https://apalabrados-isabely.herokuapp.com/)

##  Instructions to Download

1. In the [Aplabrados Repo](https://github.com/isabelyb/apalabrados)

2. Extract

3. Install

4. To run in local:

5. To **deploy in Heroku** go to the website instructions [here](https://devcenter.heroku.com/articles/getting-started-with-python).




