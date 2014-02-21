var HOST = 'raspberrypi';
var PORT = 33480;
var qURL = 'http://' + HOST + ':' + PORT + '/';

var lastSpeed = 50;
var lastSteer = 50;

function queryURL(url) {
$.ajax(url, function (response) {
  console.log(response);
});
}

function SpeedChanged(slider) {
  var out = document.getElementById("speed_out")
  if (slider.value > 75 && lastSpeed <= 75) {
    out.innerHTML = "Speed: Driving forward"
    lastSpeed = slider.value;
    queryURL(qURL + 'driveForward');
  } else if (slider.value < 25 && lastSpeed >= 25) {
    out.innerHTML = "Speed: Driving backwards"
    lastSpeed = slider.value;
    queryURL(qURL + 'driveBackward');
  } else if(slider.value >= 25 && slider.value <=75 && (lastSpeed > 75 || lastSpeed < 25)){
    out.innerHTML = "Speed: Standing still"
    lastSpeed = slider.value;
    queryURL(qURL + 'driveStop');
  }
}

function SteeringChanged(slider) {
  var out = document.getElementById("steer_out")
  if (slider.value > 75 && lastSteer <= 75) {
    out.innerHTML = "Direction: Steering right"
    lastSteer = slider.value;
    queryURL(qURL + 'steerRight');
  } else if (slider.value < 25 && lastSteer >= 25) {
    out.innerHTML = "Direction: Steering left"
    lastSteer = slider.value;
    queryURL(qURL + 'steerLeft');
  } else if(slider.value >= 25 && slider.value <=75 && (lastSteer > 75 || lastSteer < 25)){
    out.innerHTML = "Direction: Straight"
    lastSteer = slider.value;
    queryURL(qURL + 'steerStraight');
  }
}
