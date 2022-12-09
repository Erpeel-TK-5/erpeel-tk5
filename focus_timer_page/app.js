const formResponses = document.getElementsByName('formFocusTimer');

const timer = document.querySelector('.timer');
const deadline = document.querySelector('.deadline');
const items = document.querySelectorAll('.deadline-format h4');

const hours = formResponses.getHours();
const minutes = formResponses.getMinutes();
const seconds = formResponses.getSeconds();

timer.textContent = `timer ends on ${hours}:${minutes}:${seconds}`;

const futureTime = hours * 3600 * 1000 + minutes * 60 * 1000 + seconds * 1000;
function getRemaindingTime() {
  const today = 0

  const t = futureTime - today;
  // 1s = 1000ms
  // 1m = 60s
  // 1hr = 60m
  // values in miliseconds
  const oneHour = 60 * 60 * 1000;
  const oneMinute = 60 * 1000;
  // calculate all values
  let hours = Math.floor((t % oneDay) / oneHour);
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
    deadline.innerHTML = `<h4 class="expired">sorry, this timer has expired!</h4>`;
  }
}
// countdown;
let countdown = setInterval(getRemaindingTime, 1000);
//set initial values
getRemaindingTime();
