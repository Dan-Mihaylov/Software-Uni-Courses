function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/phonebook/';
    const baseDeleteUrl = 'http://localhost:3030/jsonstore/phonebook/';

    const phoneBookEl = document.getElementById('phonebook');
    document.getElementById('btnLoad').addEventListener('click', loadPhoneNumbers);
    document.getElementById('btnCreate').addEventListener('click', createPhoneNumber);

    async function loadPhoneNumbers(event) {
        phoneBookEl.innerHTML = '';

        const response = await fetch(baseUrl);
        const responseData = await response.json();

        Object.entries(responseData).forEach(entry => {
            const key = entry[0];
            const phoneData = entry[1];

            const liElement = document.createElement('li');
            liElement.textContent = `${phoneData.person}: ${phoneData.phone}`;

            const buttonEl = document.createElement('button');
            buttonEl.setAttribute('data-key', key);
            buttonEl.textContent = 'Delete';
            buttonEl.addEventListener('click', deletePhone);
            
            liElement.append(buttonEl);

            phoneBookEl.append(liElement);
        })
    }

    async function deletePhone(event) {
        const entryId = event.target.getAttribute('data-key');
        const options = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        }

        try {
            const response = await fetch(baseDeleteUrl + entryId, options);
            event.target.parentNode.remove();
        } catch (error) {
            console.error(error.message);
        }
    }

    async function createPhoneNumber(event) {
        const [personElement, phoneElement] = document.querySelectorAll('input[type="text"]');

        if (!personElement.value || !phoneElement.value) {
            return;
        }

        const entryObject = {
            person: personElement.value,
            phone: phoneElement.value
        }

        personElement.value = '';
        phoneElement.value = '';

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(entryObject)
        }

        try {
            const response = await fetch(baseUrl, options);
            loadPhoneNumbers();
        } catch (error) {
            console.error(error.message);
        }
    }
}

attachEvents();
