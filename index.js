var express = require("express");
var app = express();
var path = require('path')
var processRoute = require('./routes/process');

app.use('/speak', processRoute);

app.get('/', (req, res, next) => {
  res.sendFile(path.join(__dirname, 'public/loading.html'));
})
app.use(express.static(path.join(__dirname, 'public')));


app.get('/welcome', (req, res, next) => {
  res.sendFile(path.join(__dirname, 'public/index.html'))
})
app.get('/main', (req, res, next) => {
  res.sendFile(path.join(__dirname, 'public/main.html'));
})

app.listen(5000, () => {
  console.log('Bot is listening on port 5000!')
})
