from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def hello():
    user_ip = request.remote_addr
    return render_template('hello.html')