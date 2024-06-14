from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/travel-time-minimization')
def travel_time_minimization():
    return render_template('travel-time-minimization.html')
