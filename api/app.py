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

@app.route('/videos/<name>/<season>/<episode>')
def video_route(name, season, episode):
    response = supabase_client.table('movies').select('*').eq('name', name).eq('season', season).eq('episode', episode).execute()
    if len(response.data) == 0:
        return render_template('page_404.html')
    url = response.data[0]['link']
    return render_template('video.html', url=url)