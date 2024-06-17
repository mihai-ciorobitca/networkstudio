from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__, template_folder='templates')

links = {
    "Mr. Robot Season 1 Episode 1": "https://jumpshare.com/embed/3YfW74SSdJQ8rjFRbVf6",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/videos')
def videos():
    return render_template('videos.html', links)

@app.route('/travel-time-minimization')
def travel_time_minimization():
    return redirect('https://travel-time-minimization.vercel.app')

@app.route('/assets/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.template_folder + '/assets', filename)
