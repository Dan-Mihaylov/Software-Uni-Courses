const baseUrl = 'http://localhost:3030/jsonstore/matches/';

const addMatchButtonEl = document.getElementById('add-match');
const editMatchButtonEl = document.getElementById('edit-match');
const loadBtnEl = document.getElementById('load-matches');

const hostInputEl = document.getElementById('host');
const scoreInputEl = document.getElementById('score');
const guestInputEl = document.getElementById('guest');

const matchUlEl = document.getElementById('list');
const matchLiEl = document.querySelector('#list li.match');

matchUlEl.innerHTML = '';

loadBtnEl.addEventListener('click', loadMatches);
addMatchButtonEl.addEventListener('click', addMatch);
editMatchButtonEl.addEventListener('click', editMatchInfo);

async function loadMatches(event) {
    editMatchButtonEl.setAttribute('disabled', 'disabled');
    addMatchButtonEl.removeAttribute('disabled');
    matchUlEl.innerHTML = '';

    try {
        const response = await fetch(baseUrl);
        const responseJson = await response.json();
        const responseData = Object.values(responseJson);

        responseData.forEach(data => {
            createMatchEl(data.host, data.score, data.guest, data._id);
        })
    } catch (error) {
        console.error(error);
    }
}

function createMatchEl(host, score, guest, id) {
    const currLiEl = matchLiEl.cloneNode(true);
    const [hostEl, scoreEl, guestEl] = currLiEl.querySelectorAll('.info p');
    const [changeBtnEl, deleteBtnEl] = currLiEl.querySelectorAll('.btn-wrapper button');

    hostEl.textContent = host;
    scoreEl.textContent = score;
    guestEl.textContent = guest;

    changeBtnEl.addEventListener('click', (e) => changeMatchInfo(e,host, score, guest, id));
    deleteBtnEl.addEventListener('click', (e) => deleteMatchInfo(id));

    matchUlEl.appendChild(currLiEl);
}

async function editMatchInfo(event) {
    const host = hostInputEl.value;
    const score = scoreInputEl.value;
    const guest = guestInputEl.value;
    const id = event.target.getAttribute('data-id');

    event.target.removeAttribute('data-id');
    console.log(id);

    if (!host || !score || !guest) {
        return;
    }

    clearInputs();

    const options = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({host, score, guest, '_id': id})
    }

    try {
        const response = await fetch(baseUrl + id, options);
        
        if (!response.ok) {
            throw new Error('Error editing match info');
        }

        loadMatches();

    } catch(error) {
        console.error(error)
    }
}

function changeMatchInfo(event, host, score, guest, id) {
    editMatchButtonEl.removeAttribute('disabled');
    addMatchButtonEl.setAttribute('disabled', 'disabled');
    editMatchButtonEl.setAttribute('data-id', id);

    hostInputEl.value = host;
    scoreInputEl.value = score;
    guestInputEl.value = guest;

}

async function deleteMatchInfo(id) {
    const options = {
        method: 'DELETE'
    }

    try {
        const response = await fetch(baseUrl + id, options);
        if (!response.ok) {
            throw new Error('Error deleting record.')
        }
        loadMatches();
    } catch (error) {
        console.error(error);
    }
}

async function addMatch(event) {
    const host = hostInputEl.value;
    const score = scoreInputEl.value;
    const guest = guestInputEl.value;

    if (!host || !guest || !score) {
        return;
    }

    clearInputs();

    const newRecord = {
        host,
        score,
        guest
    }

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newRecord)
    }

    try {
        const response = await fetch(baseUrl, options);

        if (!response.ok) {
            throw new Error('Error adding record.')
        }
        loadMatches();
    } catch (error) {
        console.error(error);
    }
}

function clearInputs() {
    hostInputEl.value = '';
    scoreInputEl.value = '';
    guestInputEl.value = '';
}