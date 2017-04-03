import json
import random
from flask import Flask, render_template, request, Response
app = Flask(__name__)


### Page Rendering

@app.route('/')
def index():
    """
    Loads the index page.
    """
    return render_template('controller.html')

@app.route('/j')
def j():
    return render_template('j.html')

@app.route('/p')
def p():
    return render_template('p.html')

@app.route('/s')
def s():
    return render_template('s.html')


### Data Updates

@app.route('/slider1/<user>')
def slider1(user):
    global user_data

    user_data[user]["slider1"] = request.args["value"]

    return ""

@app.route('/slider2/<user>')
def slider2(user):
    global user_data

    user_data[user]["slider2"] = request.args["value"]

    return ""

@app.route('/slider3/<user>')
def slider3(user):
    global user_data

    user_data[user]["slider3"] = request.args["value"]

    return ""

@app.route('/increment/<user>')
def increment(user):
    global user_data
    user_data[user]["value"] += 1
    return ""

@app.route('/decrement/<user>')
def decrement(user):
    global user_data
    user_data[user]["value"] -= 1
    return ""

@app.route('/random_float/<user>')
def random_float(user):
    global user_data
    user_data[user]["random_float"] = random.random()
    return ""

@app.route('/random_int/<user>')
def random_int(user):
    global user_data
    user_data[user]["random_int"] = random.randint(0, 99)
    return ""


### Get User Data

@app.route('/get/<user>')
def get_all_values(user):
    global user_data
    return json.dumps(user_data[user])

@app.route('/get/<user>/<kind>')
def get_value(user, kind):
    global user_data
    return str(user_data[user][kind])


### Reset User Data

@app.route('/reset/<user>')
def reset(user):
    global user_data

    user_data[user] = {
            "slider1" : 0,
            "slider2" : 0,
            "slider3" : 0,
            "value" : 0,
            "random_float": 0.0,
            "random_int" : 0
    }

    return "Reset data for user: '" + user + "'"



### Initialization

user_data = {}
reset("j")
reset("p")
reset("s")





# Skyspace

@app.route('/test', methods=["POST"])
def test():
    print(request.data)
    return ""

@app.route('/skyspace/set/<mode>')
def set_mode(mode):
    global skyspace_mode

    skyspace_mode = mode

    return ""

@app.route('/skyspace/mode')
def get_mode():
    global skyspace_mode

    return skyspace_mode

skyspace_mode = ""
