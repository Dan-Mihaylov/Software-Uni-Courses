function lockedProfile() { 

    Array.from(document.querySelectorAll('.profile'))
        .forEach(profile => {
            profile.querySelector('input[value="lock"]').addEventListener('click', (e)=>{
                const button = profile.querySelector('button').removeEventListener('click', buttonClicked);
            })

            profile.querySelector('input[value="unlock"]').addEventListener('click', (e)=>{
                profile.querySelector('button').addEventListener('click', buttonClicked);
            })
        })

    function buttonClicked(event) {
        const hiddenInfoElement = event.target.parentNode.querySelector('div');
        const display = hiddenInfoElement.style.display;
        const buttonText = event.target.textContent;

        display === 'none' || display === '' ? hiddenInfoElement.style.display = 'block' : hiddenInfoElement.style.display = 'none';
        buttonText === 'Show more' ? event.target.textContent = 'Hide it' : event.target.textContent = 'Show more';
    }
}