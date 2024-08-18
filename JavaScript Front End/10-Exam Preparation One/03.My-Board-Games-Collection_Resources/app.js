const nameInputEl = document.getElementById('g-name');
const typeInputEl = document.getElementById('type');
const playersInputEl = document.getElementById('players');

const addGameBtnEl = document.getElementById('add-game');
addGameBtnEl.addEventListener('click', addGame);

const editGameBtnEl = document.getElementById('edit-game');
editGameBtnEl.addEventListener('click', editGame);

const boardGameDivEl = document.querySelector('.board-game');
const blueprintBoardGameEl = boardGameDivEl.cloneNode(true);
boardGameDivEl.remove();

const gamesListEl = document.getElementById('games-list');
document.getElementById('load-games').addEventListener('click', loadGames);

const baseUrl = 'http://localhost:3030/jsonstore/games/'


async function loadGames(){
    
    editGameBtnEl.setAttribute('disabled', 'disabled');
    addGameBtnEl.removeAttribute('disabled');
    clearGamesList();
    
    const response = await fetch(baseUrl);
    const responseJson = await response.json();
    const values = Object.values(responseJson);
    
    values.forEach(game => {
        createGameElements(game._id, game.name, game.type, game.players);
    })
    
}


function createGameElements(id, name, type, players) {
    
    currBoardEl = blueprintBoardGameEl.cloneNode(true);
    currBoardEl.setAttribute('data-id', id);
    
    const [gameNameEl, gameTypeEl, playersEl] = currBoardEl.querySelectorAll('.content p');
    
    gameNameEl.textContent = name;
    gameTypeEl.textContent = type;
    playersEl.textContent = players;
    
    const [changeButtonEl, deleteButtonEl] = currBoardEl.querySelectorAll('.buttons-container button');
    changeButtonEl.addEventListener('click', () => changeGameInfo(id, name, type, players));
    deleteButtonEl.addEventListener('click', () => deleteGame(id));
    
    gamesListEl.append(currBoardEl);
    
}

async function changeGameInfo(id, name, type, players) {
    editGameBtnEl.removeAttribute('disabled');
    addGameBtnEl.setAttribute('disabled', 'disabled');

    nameInputEl.value = name;
    typeInputEl.value = type;
    playersInputEl.value = players;

    const formEl = document.querySelector('#form form');
    formEl.setAttribute('data-id', id);
}

async function deleteGame(id) {
    const options = {
        method: 'DELETE'
    }
    try {
        const response = await fetch(baseUrl + id, options);
        if (!response.ok) {
            throw Error('Something went wrong with deleting');
        }
        loadGames();
    } catch (error) {
        console.error(error);
    }
}

function clearGamesList() {
    gamesListEl.innerHTML = '';
}

async function addGame() {
    const gameName = nameInputEl.value;
    const gameType = typeInputEl.value;
    const maxPlayers = playersInputEl.value;

    clearForm();
    
    if (!gameName.trim() || !gameType.trim() || !maxPlayers) {
        return;
    }
    
    const objectToCreate = {
        'name': gameName,
        'type': gameType,
        'players': maxPlayers
    }
    
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(objectToCreate)
    }
    try {
        const response = await fetch(baseUrl, options);
        
        if (!response.ok) {
            throw Error('Error creating new game.');
        }
        loadGames();
    } catch (error) {
        console.error(error);
    }   
}

async function editGame() {
    const name = nameInputEl.value;
    const type = typeInputEl.value;
    const players = playersInputEl.value;
    const id = document.querySelector('#form form').getAttribute('data-id');
    
    clearForm();

    objectInfo = {
        name,
        type,
        players
    }

    const options = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(objectInfo)
    }

    try {
        const response = await fetch(baseUrl + id, options);
        if (!response.ok) {
            throw Error('Error editing item');
        }
        loadGames();
    } catch (error) {
        console.error(error);
    }

}

function clearForm() {
    nameInputEl.value = '';
    typeInputEl.value = '';
    playersInputEl.value = '';
}
