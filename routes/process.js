var route = require('express').Router();
const { exec } = require('child_process');

route.get('/:msg/:lang', (req, res) => {
  var input = req.params.msg;
  var lang = req.params.lang;
  if(lang == "hi") {
    var heyPy = exec(`python3 index.py ${input}`, function (error, stdout, stderr) {
      if (error) {
        console.log(error.stack);
        console.log('Error code: '+error.code);
        console.log('Signal received: '+error.signal);
      }
      console.log('Child Process STDOUT: '+stdout);
      console.log('Child Process STDERR: '+stderr);
    });

    heyPy.on('exit', function (code) {
      console.log('Child process exited with exit code '+code);
    });
  } else {
    var heyPy = exec(`python3 index.en.py ${input}`, function (error, stdout, stderr) {
      if (error) {
        console.log(error.stack);
        console.log('Error code: '+error.code);
        console.log('Signal received: '+error.signal);
      }
      console.log('Child Process STDOUT: '+stdout);
      console.log('Child Process STDERR: '+stderr);
    });

    heyPy.on('exit', function (code) {
      console.log('Child process exited with exit code '+code);
    });
  }
  res.send('ok')
})

module.exports = route;
