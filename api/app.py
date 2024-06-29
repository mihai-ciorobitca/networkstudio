from flask import Flask, render_template, send_from_directory, redirect
from supabase import create_client, Client

URL_BASE = 'https://qfvhxwctxqrtemtysrrx.supabase.co'
SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFmdmh4d2N0eHFydGVtdHlzcnJ4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxOTY2MzAzMiwiZXhwIjoyMDM1MjM5MDMyfQ.JZ9YSF8o-Jgmxv0ePW4suSsYyD_KmPIpgxqrPrjQpNA'

supabase_client: Client = create_client(URL_BASE, SECRET_KEY)

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/travel-time-minimization')
def travel_time_minimization():
    return redirect('https://travel-time-minimization.vercel.app')

def create_route(endpoint, url):
    def generic_route():
        return render_template('video.html', url=url)
    app.add_url_rule(f'/{endpoint}', endpoint, generic_route)

@app.route('/videos/', defaults={'name': None, 'season': None, 'episode': None})
@app.route('/videos/<name>/', defaults={'season': None, 'episode': None})
@app.route('/videos/<name>/<season>/', defaults={'episode': None})
@app.route('/videos/<name>/<season>/<episode>/')
def video_route(name, season, episode):
    query = supabase_client.table('movies').select('*')
    
    if name:
        query = query.eq('name', name)

    if season:
        query = query.eq('season', season)
        
    if episode:
        query = query.eq('episode', episode)
        
    response = query.execute()
    
    if len(response.data) == 0:
        return render_template('page_404.html')
    
    if not name and not season and not episode:
        names = list(set(map(lambda x: x["name"], response.data)))
        return render_template('names.html', names=names)
    elif not season and not episode:
        seasons = list(set(map(lambda x: x["season"], response.data)))
        return render_template('seasons.html', seasons=seasons, name=name)
    elif season and not episode:
        episodes = list(set(map(lambda x: x["episode"], response.data)))
        return render_template('episodes.html', episodes=episodes, name=name, season=season)
    else:
        url = response.data[0]['link']
        return render_template('video.html', url=url)
