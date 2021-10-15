from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')


@app.route('/data/<table>')
def data(table):
    return render_template('numbers.html', table=table)


if __name__ == '__main__':
    app.run(debug=True)