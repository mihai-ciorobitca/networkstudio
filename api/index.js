const express = require('express');
const path = require('path');
const apicache = require('apicache');
const cors = require("cors");

const info = [{
        "title": "Where to host my website?",
        "text": "Use Vercel or Render for FREE"
    },
    {
        "title": "I lost my phone, what can I do?",
        "text": "Use Globfone to make a call for free"
    },
    {
        "title": "How to download videos free?",
        "text": "Convert m3u8 file into mp4"
    },
    {
        "title": "How to style my website?",
        "text": "Use Bootstrap framework"
    },
    {
        "title": "What to use for real time chat app?",
        "text": "Socket IO technology"
    },
    {
        "title": "How to host real time chat app?",
        "text": "Upload docker container on Render"
    },
]

const app = express();

const cache = apicache.middleware;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.use(cors({
    origin: 'https://networkstudio.store',
}));

app.get('/', (req, res) => {
    res.render('index', { info: info });
});

app.get('/resume', (req, res) => {
    res.render('resume');
});

app.use((req, res, next) => {
    res.status(404).render('page_404');
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on http://127.0.0.1:${port}`);
});