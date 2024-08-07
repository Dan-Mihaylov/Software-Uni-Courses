function solve() {
    const infoBoard = document.getElementById('info').children[0];
    const buttonDepartElement = document.getElementById('depart');
    const buttonArriveElement = document.getElementById('arrive');

    const baseUrl = 'http://localhost:3030/jsonstore/bus/schedule/';

    function depart() {
        const currentStationId = 
            infoBoard.hasAttribute('data-next-stop-id')
            ?
            infoBoard.getAttribute('data-next-stop-id')
            :
            'depot';
        
        fetch(baseUrl + currentStationId)
            .then(response => response.json())
            .then(stop => {
                infoBoard.textContent = `Next stop ${stop.name}`;
                infoBoard.setAttribute('data-next-stop-id', stop.next);
                buttonDepartElement.disabled = true;
                buttonArriveElement.disabled = false;
            })

    }

    async function arrive() {
        const  destinationName = infoBoard.textContent.split('Next stop ')[1];
        infoBoard.textContent = `Arriving at ${destinationName}`;

        buttonArriveElement.disabled = true;
        buttonDepartElement.disabled = false;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
