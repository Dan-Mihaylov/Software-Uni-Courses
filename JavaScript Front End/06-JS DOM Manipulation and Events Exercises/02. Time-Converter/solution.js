function attachEventsListeners() {

    function findSeconds(description, number) {
        const convertToSeconds = {
            'days': (numberDays) => numberDays * 24 * 60 * 60,
            'hours': (numberHours) => numberHours * 60 * 60,
            'minutes': (numberMinutes) => numberMinutes * 60,
            'seconds': (numberSeconds) => numberSeconds
        }

        return convertToSeconds[description](Number(number));
    }

    function findAllFromSeconds(seconds) {
        const days = seconds / 60 / 60 / 24;
        const hours = seconds / 60 / 60;
        const minutes = seconds / 60;

        return [days, hours, minutes, seconds];
    }
    
    Array.from(document.querySelectorAll('input[type="button"]'))
        .forEach(button => {
            button.addEventListener('click', (e)=>{
                const number = Number(e.target.parentNode.querySelector('input[type="text"]').value);
                const description = e.target.parentNode.querySelector('input[type="text"]').id;

                let convertedToSeconds = findSeconds(description, number);

                const [days, hours, minutes, seconds] = findAllFromSeconds(convertedToSeconds);
                
                document.getElementById('days').value = days;
                document.getElementById('hours').value = hours;
                document.getElementById('minutes').value = minutes;
                document.getElementById('seconds').value = seconds;
               
            })
        });
}