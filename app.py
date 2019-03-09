import os, time
from flask import Flask, render_template, jsonify
import geojson

app = Flask(__name__)
app.debug = True

MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')

@app.route('/')
def index():
    return render_template('index.html', MAPBOX_TOKEN=MAPBOX_TOKEN)

@app.route('/earthquakes_data')
def get_data():
    with open('data.geojson', 'r') as f_in:
        contents = f_in.read()
        feature_collection = geojson.loads(contents)
    return jsonify(result=feature_collection)

app.run(threaded=True)
