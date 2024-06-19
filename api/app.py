from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__, template_folder='templates')

routes = {
    "Mr.Robot/Season1/Episode1": "https://jumpshare.com/embed/3YfW74SSdJQ8rjFRbVf6",
    "Mr.Robot/Season1/Episode2": "https://jumpshare.com/embed/7stUTPqXwLby4vekXRSD",
    "Mr.Robot/Season1/Episode3": "https://jumpshare.com/embed/nYu50wipdpx2CHccn65i",
    "Mr.Robot/Season1/Episode4": "https://jumpshare.com/embed/xTb55Cuco8EGwhDk63s8",
    "Mr.Robot/Season1/Episode5": "https://jumpshare.com/embed/GDkkFM0IN2QXb3smTDFg",
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