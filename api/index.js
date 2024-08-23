require('dotenv').config();
const express = require('express');
const { createClient } = require('@supabase/supabase-js');
const path = require('path');
const apicache = require('apicache');

const URL_BASE = process.env.URL_BASE;
const SECRET_KEY = process.env.SECRET_KEY;

const supabaseClient = createClient(URL_BASE, SECRET_KEY);
const app = express();

// Initialize cache with apicache
const cache = apicache.middleware;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  // Homepage
  res.render('index');
});

app.get('/login', (req, res) => {
  // Login
  res.render('login');
});

app.get('/travel-time-minimization', (req, res) => {
  // Redirect to the Travel Time Minimization application
  res.redirect('https://travel-time-minimization.vercel.app');
});

app.use((req, res, next) => {
  // Page not found
  res.status(404).render('page_404');
});

app.get(['/videos/', '/videos/name=:name/', '/videos/name=:name/part=:part/', '/videos/name=:name/season=:season/', '/videos/name=:name/season=:season/episode=:episode/'], cache('10 minutes'), async (req, res) => {
  const { name, season, episode, part } = req.params;
  let query = supabaseClient.from('movies').select('*');
  
  if (name) {
    query = query.eq('name', name);
    if (season) {
      query = query.eq('season', season);
      if (episode) {
        const response = await query.order('episode').execute();
        const episodes = response.data;
        const indexVariable = episodes.findIndex(d => d.episode == episode);
        let prevUrl = '';
        let nextUrl = '';

        if (indexVariable > 0) {
          const prevEpisode = episodes[indexVariable - 1].episode;
          prevUrl = `/videos/name=${name}/season=${season}/episode=${prevEpisode}/`;
        }

        if (indexVariable < episodes.length - 1) {
          const nextEpisode = episodes[indexVariable + 1].episode;
          nextUrl = `/videos/name=${name}/season=${season}/episode=${nextEpisode}/`;
        }

        const url = episodes[indexVariable].link;
        return res.render('video', { name, season, episode, url, prevUrl, nextUrl });
      } else {
        const response = await query.execute();
        const episodes = [...new Set(response.data.map(item => item.episode))].sort();
        return res.render('episodes', { episodes, name, season });
      }
    }

    if (part) {
      const response = await query.order('part').execute();
      const parts = response.data;
      const indexVariable = parts.findIndex(d => d.part == part);
      let prevUrl = '';
      let nextUrl = '';

      if (indexVariable > 0) {
        const prevPart = parts[indexVariable - 1].part;
        prevUrl = `/videos/name=${name}/part=${prevPart}/`;
      }

      if (indexVariable < parts.length - 1) {
        const nextPart = parts[indexVariable + 1].part;
        nextUrl = `/videos/name=${name}/part=${nextPart}/`;
      }

      const url = parts[indexVariable].link;
      return res.render('video', { name, part, url, prevUrl, nextUrl });
    }

    const response = await query.execute();
    const seasons = [...new Set(response.data.map(item => item.season))].sort();
    if (seasons[0]) {
      return res.render('seasons', { seasons, name });
    }

    const parts = [...new Set(response.data.map(item => item.part))].sort();
    return res.render('parts', { parts, name });
  }

  const response = await query.execute();
  const names = [...new Set(response.data.map(item => item.name))].sort();
  return res.render('names', { names });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server running on http://127.0.0.1:${port}`);
});
