# Apalabrados

**Apalabrados** is a nice database to save the user input and store it according to the data type.
* **Numbers:** It saves your input and accumulates with the last accumulated.
* **Text:** It saves your input and its first and last character.
* **Special characters:** It saves it from your input, only the special characters.

This Web App is part of challenge of diagnostic in Platzi Master Cohort[8].

## How to use it

* **Step 1:** go to [Home](https://apalabrados-isabely.herokuapp.com/) and insert and input you want.![home](/assets/home.jpg)

* **Step 2:** When you have submitted an input **Apalabrados** redirect to app [response](https://apalabrados-isabely.herokuapp.com/submit).
There you can see the result of database that is saved and proceced yhe input according to the data type. ![submit](/assets/submit.jpg)

You could go to back to the home and try the times you want!

## How to I made it

To develop this app I followed this steps in its order.

1. Made a github [repository](https://github.com/isabelyb/apalabrados).
2. Made a first version of the process with data flowchart. Then I have to adjust some details i nthe develop app process. ![data_process](/assets/apalabrados_flowchart.drawio.svg)
4. How I feel more comfortable with Python, I looked for a better way to do a Web App using it. I found the more efficient tool was Flask, so I learned from zero how to do it.
I read a lot of sources, these were the most helpful for me:
    * [Platzi](https://platzi.com/clases/flask/)
    * [Documentation](https://palletsprojects.com/p/flask/)
    * [Pythonise tutorial](https://pythonise.com/series/learning-flask/flask-application-structure)
    * [python-adv-web-apps](https://python-adv-web-apps.readthedocs.io/en/latest/flask.html)
4. Made a first version of the App structure. As the _proces data flowchart_ I have to adjust some details in the develop app process. Too, I use [drawio](https://app.diagrams.net/) to do it.![app_structure](/assets/app.drawio.svg)
5. Looked for learning about how to connect MongoDB with a Flask App. Some time ago I have learned about some basics from mongo in [Platzi](https://platzi.com/clases/mongodb/).
    [Mongodb](https://docs.mongodb.com/)
    [Pythonbasics tutorial](https://pythonbasics.org/flask-mongodb/)
6. Code! _By the way, my computer runs Ubuntu 20.04._
    &nbsp;    
    6.1. Create a virtual environment: ```virtualenv venv``` -> ```source venv/bin/activate```
    &nbsp;
    6.2. Install Flask: ```pip3 install Flask```
    
    &nbsp;
    
    6.3. Create file main.py in order to start my web app.
    
    &nbsp;
    
    6.4. Config environment variables from the command line.
        ```export FLASK_APP=main.py``` -> Define to run Web App from main.py
        ```export FLASK_DEBUG=1```     -> Turn the debugger on to follow the Web App development.
    &nbsp;
    
    6.5. Run Flask to try the Web App: ```flask run```
    6.6. Saved requirements.txt. Update every tool installation: ```pip3 freeze > requirements.txt```
    &nbsp;
    
    6.7. Create database in mongodb:
        [mongo_db](/assets/mongo_db.jpg)
    &nbsp;
    
    6.8. Install Flask-PyMongo and conect database with the Web App.
    &nbsp;
    
    6.9. Create the Python code to manage data from the user Input with Mongodb. I used pandas too, to do it.
        1. Methods POST and GET to send and get data with Web App from mongodb.
        2. Create a classifier function to save all data in the right mongo collection according to the datatype.
        3. Create a function to get updated data from mongo and render in HTML table to show in the Web App. I use [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) to do it.
        5. Last details in basic HTML with code to show the information in the Web App. I use the [Jinja Templates](https://jinja.palletsprojects.com/en/3.0.x/templates/) to do this.


## Deploy in [HEROKU](https://www.heroku.com/)

1. Created ```runtime.txt``` file: This is requierement to set the Python version to run the Web App.
2. Install the web server for Python [gunicorn](https://gunicorn.org/) and created the ```procfile``` file in order to [specify to heroku](https://devcenter.heroku.com/articles/procfile) how to start the App.
3. Install the [Heroku Command Line](https://devcenter.heroku.com/categories/command-line) to perform the App in Heroku.
4. Made the integration of my GitHub repository [with Heroku](https://devcenter.heroku.com/articles/github-integration).

My Web App was deployed and I felt so happy for this. 
        [deploy](/assets/deploy.jpg)
This is my first App complet from zero to deploy.


Finally I finished to write the README.md file.

[View **Apalabrados** deployment here](https://apalabrados-isabely.herokuapp.com/)

##  Instructions to Download

This is a brief guide, You should adapt it to your own software requirements.

1. In the [Aplabrados Repo](https://github.com/isabelyb/apalabrados), go to download zip file:

![download](/assets/download.jpg)
 

2. Extract file.
 
3. From command line, in the app root create a virtual enviroment. 

4. Inside **venv** install Web App requirements: ```pip3 install -r requirements.txt``` 

5. To run in local: 
    5.1. Config environment variables from the command line: ```export FLASK_APP=main.py``` and ```export FLASK_DEBUG=1```
    5.2. Run Flask to try the Web App: ```flask run``` 
 
6. To **deploy in Heroku** go to the website instructions [here](https://devcenter.heroku.com/articles/getting-started-with-python).




