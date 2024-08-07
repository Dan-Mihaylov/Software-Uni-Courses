function getInfo() {
    const resultDivElement = document.getElementById('result');
    const stopNameElement = document.getElementById('stopName');
    const busesUlElement = document.getElementById('buses');
    const stopIdElement = document.getElementById('stopId');
    const baseUrl = 'http://localhost:3030/jsonstore/bus/businfo/';

    // Clear the previous results
    [...resultDivElement.children].forEach(child=> child.innerHTML = '');

    // Fetch the url with the info
    const currentUrl = baseUrl + stopIdElement.value;
    fetch(currentUrl)
        .then(response => response.json())
        .then(data => {
            const stopName = data.name;
            const buses = data.buses;
            
            stopNameElement.textContent = stopName;
            createLiElements(buses);
        })
        .catch(stopNameElement.textContent = 'Error');
    
    // Create li elements
    function createLiElements(busStopInfo) {
        Object.entries(busStopInfo)
            .forEach(entry => {
                const textContent = `Bus ${entry[0]} arrives in ${entry[1]} minutes`;

                const liElement = document.createElement('li');
                liElement.textContent = textContent;

                busesUlElement.append(liElement);
            })
    }

    // Clear stop ID input
    stopIdElement.value = '';

}
