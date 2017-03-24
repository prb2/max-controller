import json
from flask import Flask, render_template, request, Response
app = Flask(__name__)

speed = 10

@app.route('/')
def index():
    """
    Loads the index page.
    """
    return render_template('controller.html')


@app.route('/speed')
def get_speed():
    print request.form

    results = {}
    results["speed"] = speed

    results_json = json.dumps(results)
    print results_json

    return Response(results_json, status=200, mimetype='application/json')

@app.route('/faster')
def faster():
    global speed
    speed += 1
    print speed
    return ""

@app.route('/slower')
def slower():
    global speed
    speed -= 1
    print speed
    return ""
