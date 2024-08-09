function attachEvents() {
    const baseUrl = ' http://localhost:3030/jsonstore/messenger';
    const textareaElement = document.getElementById('messages');

    document.getElementById('refresh').addEventListener('click', refreshContent);
    document.getElementById('submit').addEventListener('click', sendMessage);

    async function refreshContent (event) {
        const messagesResponse = await fetch(baseUrl);
        const messagesData = await messagesResponse.json();
        const messagesArray = Object.values(messagesData);
        
        const mappedData = messagesArray.map(data => `${data.author}: ${data.content}`);
        textareaElement.textContent = mappedData.join('\n');
    }

    async function sendMessage(event) {
        const senderNameEl = document.querySelector('input[name="author"]');
        const senderMessageEl = document.querySelector('input[name="content"]');

        const sendingObject = {
            "author": senderNameEl.value,
            "content": senderMessageEl.value
        }

        const jsonObject = JSON.stringify(sendingObject);

        try {
            const response = await fetch(baseUrl, {
                method: 'POST',
                body: jsonObject,
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if(!response.ok) {
                throw Error('Error on POST request', response.status)
            }

        }
        catch (error){
            console.error(error)
        }

        senderNameEl.value = '';
        senderMessageEl.value = '';
        refreshContent();
    }
}

attachEvents();