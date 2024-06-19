from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__, template_folder='templates')

routes = {
    "Mr.Robot/Season1/Episode1": "https://drive.google.com/file/d/1APwSSGQ_QIg-SmmmxhnZm8xx6AFR9yQf/preview",
    "Mr.Robot/Season1/Episode2": "https://drive.google.com/file/d/11Dkz-7afKeT8GCa0aoYoZQ4z5iZnMe7B/preview",
    "Mr.Robot/Season1/Episode3": "https://drive.google.com/file/d/1XJ7zoFwyju2ksBa98IgMb724lZb3PQiQ/preview",
    "Mr.Robot/Season1/Episode4": "https://drive.google.com/file/d/1oGCDrpOtR-1pyqVq-dE5lwM8fVG8PSH8/preview",
    "Mr.Robot/Season1/Episode5": "https://drive.google.com/file/d/1HOblgXpeyWQ2AJTizBjrabTt9oaiC-PL/preview",
    "Mr.Robot/Season1/Episode6": "https://drive.google.com/file/d/1juTMfI_L_kcQsqsX4yB2Xolc5hHTUn_q/preview",

}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/travel-time-minimization')
def travel_time_minimization():
    return redirect('https://travel-time-minimization.vercel.app')

@app.route('/assets/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.template_folder + '/assets', filename)

def create_route(endpoint, url):
    def generic_route():
        return render_template('video.html', url=url)
    app.add_url_rule(f'/{endpoint}', endpoint, generic_route)

[create_route(endpoint, url) for endpoint, url in routes.items()]