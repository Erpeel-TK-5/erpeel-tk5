const formResponses = document.getElementsByName('formFocusTimer');

const timer = document.querySelector('.timer');
const deadline = document.querySelector('.deadline');
const items = document.querySelectorAll('.deadline-format h4');

var query = window.location.search.substring(1);
var hour = document.getElementById('hours').innerHTML;
var minute = document.getElementById('minutes').innerHTML;
var second = document.getElementById('seconds').innerHTML;

const hours = parseInt(hour);
const minutes = parseInt(minute);
const seconds = parseInt(second);

const duration = hours * 3600 * 1000 + minutes * 60 * 1000 + seconds * 1000;
const futureTime = new Date().getTime() + duration;
function getRemaindingTime() {
  console.log("call");
  const today = new Date().getTime();
  const t = futureTime - today;
  // 1s = 1000ms
  // 1m = 60s
  // 1hr = 60m
  // values in miliseconds
  const oneHour = 60 * 60 * 1000;
  const oneMinute = 60 * 1000;
  // calculate all values
  let hours = Math.floor(t/oneHour % 24);
  let minutes = Math.floor((t % oneHour) / oneMinute);
  let seconds = Math.floor((t % oneMinute) / 1000);
  // set values array
  const values = [hours, minutes, seconds];
  function format(item) {
    if (item < 10) {
      return (item = `0${item}`);
    }
    return item;
  }
  items.forEach(function (item, index) {
    item.innerHTML = format(values[index]);
  });
  if (t < 0) {
    clearInterval(countdown);
    console.log(navigator.languages);
    deadline.innerHTML = `<div class="deadline-format">
    <div>
      <h4 id="hours">00</h4>
    </div>
  </div>
  <!-- end of hours -->
  <!-- minutes -->
  <div class="deadline-format">
    <div>
      <h4 id="minutes">00</h4>
    </div>
  </div>
  <!-- end of minutes -->
  <!-- seconds -->
  <div class="deadline-format">
    <div>
      <h4 id="seconds">00</h4>
    </div>
  </div>`;
  }
}
// countdown;
let countdown = setInterval(getRemaindingTime, 1000);
//set initial values
getRemaindingTime();
