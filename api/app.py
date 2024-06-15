from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/travel-time-minimization')
def travel_time_minimization():
    return render_template('travel-time-minimization.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/assets/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.template_folder + '/assets', filename)
