const winPatterns = [
  {
    'name': 'Full House',
    'validator': fullHouseValidator
  }, 
  {
    'name': 'Top Row',
    'validator': topRowValidator
  },
  {
    'name': 'Early 5',
    'validator': earlyValidator
  }
];

function fullHouseValidator(ticket) {
  return !ticket.data.flat().some((item) => item !== '-' && item !== 'x');
}

function topRowValidator(ticket) {
  return !ticket.data[0].some((item) => item !== '-' && item !== 'x');  
}

function earlyValidator(ticket) {
  return ticket.data.flat().filter(item => item === "x").length >= 5;
}

showWinners();

async function showWinners() {
  const tickets = await getTickets();
  const markedNums = await getMarkedNums();
  const markedTickets = tickets.map(ticket => markTicket(ticket, markedNums));

  const rootDiv = document.getElementById('win_patterns');
  rootDiv.innerHTML = "";
  for(let i = 0; i < winPatterns.length; i++) {
    const pattern = winPatterns[i];
    rootDiv.innerHTML += ('<div>');
    rootDiv.innerHTML += ('<h3>' + pattern.name + '</h3>');
    const wonThisPattern = markedTickets.filter(pattern.validator);
    rootDiv.innerHTML += ('<ul>');
    for(let j = 0; j < wonThisPattern.length; j++) {
      rootDiv.innerHTML += ('<li>' + wonThisPattern[j].name + '</li>');
    }
    rootDiv.innerHTML += ('</ul>');
    rootDiv.innerHTML += ('</div>');
  }
}

function markTicket(ticket, markedNums) {
  for(let i = 0; i < ticket.data.length; i++) {
    for(let j = 0; j < ticket.data[i].length; j++) {
      for(let k = 0; k < markedNums.length; k++) {
        if(ticket.data[i][j] === markedNums[k]) {
          ticket.data[i][j] = "x";
        }
      }
    }
  }
  return ticket;
}

async function getMarkedNums() {
  const response = await fetch("/games/");

  if (response.ok) { 
    const json = await response.json();
    return json.numbers.split(",");
  } else {
    console.log("HTTP-Error: " + response.status);
  }
}

async function getTickets() {
  let response = await fetch("/games/tickets/");

  if (response.ok) { 
    let json = await response.json();
    return json.map(processTicket);
  } else {
    console.log("HTTP-Error: " + response.status);
  }
}

function processTicket(ticket) {
  ticket.data = JSON.parse(ticket.data);
  return ticket;
}
