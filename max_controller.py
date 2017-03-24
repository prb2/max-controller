import json
from flask import Flask, render_template, request, Response
app = Flask(__name__)

value = 10

@app.route('/')
def index():
    """
    Loads the index page.
    """
    return render_template('controller.html')


@app.route('/value')
def get_value():
    global value
    return str(value)

@app.route('/increment')
def increment():
    global value
    value += 1
    print value
    return ""

@app.route('/decrement')
def decrement():
    global value
    value -= 1
    print value
    return ""
