var recognition = new webkitSpeechRecognition();

recognition.continuous = true;

function start(){
	recognition.onresult = function(event) {
		console.log(event);
		var output = document.getElementById("output");
		output.innerHTML = "";
		output.innerHTML = event.results[event.results.length - 1][0].transcript;
		send();
	}
	recognition.start();
}

function send() {
  $("#loader")[0].style.display = 'inherit';
  $.ajax({
    method: "GET",
    url: '/speak/'+document.getElementById("output").innerHTML
  }).done(function () {
    $("#loader")[0].style.display = 'none';
  })
}
