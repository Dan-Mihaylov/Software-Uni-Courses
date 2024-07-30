function validate() {
    
    const inputElement = document.getElementById('email');
    const regex = new RegExp(/^[a-z]+@[a-z]+.[a-z]+$/g);

    inputElement.addEventListener('change', validateEmail);

    function validateEmail(event) {
        const email = event.currentTarget.value;

        const result = email.match(regex);
        
        if (!result) {
            event.currentTarget.className = 'error';
        } else {
            event.currentTarget.className = '';
        }
    }

}