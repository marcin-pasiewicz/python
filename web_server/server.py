from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<username>')
def hello_world(username=None):
    return render_template('index.html', name=username)


@app.route('/about')
def about():
    return render_template('about.html')

