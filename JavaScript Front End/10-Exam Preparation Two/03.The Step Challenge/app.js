const baseUrl = 'http://localhost:3030/jsonstore/records/';

const loadButtonEl = document.getElementById('load-records');
loadButtonEl.addEventListener('click', loadRecords);

const recordLiEl = document.querySelector('#list li.record');
const recordsListElement = document.getElementById('list');

const addRecordButtonEl = document.getElementById('add-record');
addRecordButtonEl.addEventListener('click', addRecord);

const editRecordButtonEl = document.getElementById('edit-record');
editRecordButtonEl.addEventListener('click', editRecord);

const nameInputEl = document.getElementById('p-name');
const stepsInputEl = document.getElementById('steps');
const caloriesInputEl = document.getElementById('calories');

function clearList() {
    recordsListElement.innerHTML = '';
}
clearList();

async function loadRecords() {
    clearList();
    addRecordButtonEl.removeAttribute('disabled');
    editRecordButtonEl.setAttribute('disabled', 'disabled');

    // fetch all records
    const response = await fetch(baseUrl);
    const responseJson = await response.json();
    const responseValues = Object.values(responseJson);

    console.log(responseValues);

    for (record of responseValues) {
        createRecord(record._id, record.name, record.steps, record.calories);
    }
}


async function createRecord(id, name, steps, calories) {
    const newRecordEl = recordLiEl.cloneNode(true);
    
    const [nameEl, stepsEl, caloriesEl] = newRecordEl.querySelectorAll('p');
    
    nameEl.textContent = name;
    stepsEl.textContent = steps;
    caloriesEl.textContent = calories;

    const [changeButtonEl, deleteButtonEl] = newRecordEl.querySelectorAll('.btn-wrapper button');

    changeButtonEl.setAttribute('data-id', id);
    changeButtonEl.addEventListener('click', changeEntry);

    deleteButtonEl.setAttribute('data-id', id);
    deleteButtonEl.addEventListener('click', deleteEntry);

    recordsListElement.appendChild(newRecordEl);
}

function changeEntry(event) {
    addRecordButtonEl.setAttribute('disabled', 'disabled');
    editRecordButtonEl.removeAttribute('disabled');

    const recordEl = event.target.parentNode.parentNode;
    const [pName, steps, calories] = recordEl.querySelectorAll('.info p');

    nameInputEl.value = pName.textContent;
    stepsInputEl.value = steps.textContent;
    caloriesInputEl.value = calories.textContent;

    editRecordButtonEl.setAttribute('data-id', event.target.getAttribute('data-id'));
}

async function deleteEntry(event) {
    const id = event.target.getAttribute('data-id');

    const options = {
        method: 'DELETE'
    }

    try {
        const response = await fetch(baseUrl + id, options);

        if (!response.ok) {
            throw Error('Error deleting record!');
        }
        console.log(response);

        loadRecords();

    } catch (error) {
        console.error(error);
    }
}

async function addRecord(event) {
    const pName = nameInputEl.value;
    const steps = stepsInputEl.value;
    const calories = caloriesInputEl.value;

    if (!pName || !steps || !calories) {
        return;
    }

    clearInputFields();

    const recordObject = {
        name: pName,
        steps,
        calories
    }

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(recordObject)
    }

    try {
        const response = await fetch(baseUrl, options);
        
        if (!response.ok) {
            throw Error('Error creating new record!')
        }

        loadRecords();

    } catch (error) {
        console.error(error);
    }

}

async function editRecord(event) {
    const pName = nameInputEl.value;
    const steps = stepsInputEl.value;
    const calories = caloriesInputEl.value;
    const id = event.target.getAttribute('data-id');

    if (!pName || !steps || !calories) {
        return;
    }

    clearInputFields();

    const recordObject = {
        _id: id,
        name: pName,
        steps,
        calories
    }

    const options = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(recordObject)
    }

    try {
        const response = await fetch(baseUrl + id, options);

        if(!response.ok) {
            throw Error('Error Editing Record!');
        }
        loadRecords();

    } catch (error) {
        console.error(error);
    }

}

function clearInputFields() {
    nameInputEl.value = '';
    stepsInputEl.value = '';
    caloriesInputEl.value = '';
}
