function rowValidator(row) {
  return (t) => !t.data[row].some((cell) => cell !== '-' && cell !== 'x');
}

const winPatterns = [
  {
    name: 'Full House',
    validator: (t) =>
      !t.data.flat().some((cell) => cell !== '-' && cell !== 'x'),
  },
  {
    name: 'Top Row',
    validator: rowValidator(0),
  },
  {
    name: 'Middle Row',
    validator: rowValidator(1),
  },
  {
    name: 'Bottom Row',
    validator: rowValidator(2),
  },
  {
    name: 'Early 5',
    validator: (t) => t.data.flat().filter((cell) => cell === 'x').length >= 5,
  },
  {
    name: 'Love at first sight',
    validator: (t) =>
      markedNums.length === 1 &&
      t.data.flat().filter((cell) => cell === 'x').length === 1,
  },
];

showWinners();

async function nextNumber() {
  await fetch('/games/random/');
  location.reload();
}

async function newGame() {
  if (confirm('Start new game?')) {
    await fetch('/games/new/');
    location.reload();
  }
}

function initSpinner(markedNums) {
  let to, from;
  if (markedNums.length > 0) {
    to = markedNums[0].padStart(2, '0');
    from = (markedNums[1] || '00').padStart(2, '0');
  }
  odoo.default({ el: '.js-odoo', from, to });
}

async function showWinners() {
  initSpinner(markedNums);
  const sortedNums = [...markedNums];
  sortedNums.shift();
  document.getElementById('prev-nums-unsorted').innerHTML = sortedNums
    .slice(0, 5)
    .join(', ');
  sortedNums.sort((a, b) => a - b);
  document.getElementById('prev-nums').innerHTML = sortedNums.join(', ');

  const tickets = await getTickets();
  document.getElementById('tickets').innerHTML = `${tickets.length} tickets`;
  const markedTickets = tickets.map((ticket) => markTicket(ticket, markedNums));

  const rootDiv = document.getElementById('win_patterns');
  rootDiv.innerHTML = '';
  winPatterns.forEach((pattern) => {
    rootDiv.innerHTML += `
    <div>
      <h3>${pattern.name}</h3>
      <ul>
      ${markedTickets
        .filter(pattern.validator)
        .map((winningPattern) => `<li>${winningPattern.name}</li>`)
        .join('')}
      </ul>
    </div>`;
  });
}

function markTicket(ticket, markedNums) {
  for (let i = 0; i < ticket.data.length; i++) {
    for (let j = 0; j < ticket.data[i].length; j++) {
      if (markedNums.includes(ticket.data[i][j])) {
        ticket.data[i][j] = 'x';
      }
    }
  }
  return ticket;
}

async function getMarkedNums() {
  const response = await fetch('/games/');

  if (response.ok) {
    const json = await response.json();
    return json.numbers.split(',');
  } else {
    console.log('HTTP-Error: ' + response.status);
  }
}

async function getTickets() {
  let response = await fetch('/games/tickets/');

  if (response.ok) {
    let json = await response.json();
    return json.map(processTicket);
  } else {
    console.log('HTTP-Error: ' + response.status);
  }
}

function processTicket(ticket) {
  ticket.data = JSON.parse(ticket.data);
  return ticket;
}
