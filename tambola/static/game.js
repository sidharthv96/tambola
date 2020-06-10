const winPatterns = [
  {
    name: 'Full House',
    validator: (t) =>
      !t.data.flat().some((cell) => cell !== '-' && cell !== 'x'),
  },
  {
    name: 'Top Row',
    validator: (t) => !t.data[0].some((cell) => cell !== '-' && cell !== 'x'),
  },
  {
    name: 'Middle Row',
    validator: (t) => !t.data[1].some((cell) => cell !== '-' && cell !== 'x'),
  },
  {
    name: 'Bottom Row',
    validator: (t) => !t.data[2].some((cell) => cell !== '-' && cell !== 'x'),
  },
  {
    name: 'Early 5',
    validator: (t) => t.data.flat().filter((cell) => cell === 'x').length >= 5,
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
async function showWinners() {
  const tickets = await getTickets();
  const markedNums = await getMarkedNums();
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

const curNum = document.getElementById('cur_num').innerHTML.padStart(2, '0');
odoo.default({ el: '.js-odoo', from: '00', to: curNum });
