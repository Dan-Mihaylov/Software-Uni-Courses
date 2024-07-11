function passwordValidator(password){

    function validateLength(password){
        return 6 <= password.length && password.length <= 10;
    };

    function validateLettersAndDigitsOnly(password){
        const regex = new RegExp(/[A-Za-z0-9]/);
        for (letter of password){
            if (!regex.test(letter)){
                return false;
            };
        };

        return true;
    };

    function validateAtLeastTwoDigits(password){
        const regex = new RegExp(/[0-9]/);
        let count = 0;
        for (letter of password){
            if (regex.test(letter)) {
                count++;
            };
        };
        return count >= 2;
    };

    let errors = [];

    if (!validateLength(password)) {
        errors.push('Password must be between 6 and 10 characters');
    };

    if (!validateLettersAndDigitsOnly(password)){
        errors.push('Password must consist only of letters and digits');
    };

    if (!validateAtLeastTwoDigits(password)){
        errors.push('Password must have at least 2 digits');
    };

    if (errors.length > 0) {
        console.log(errors.join('\n'));
    } else {
        console.log('Password is valid');
    };
};

passwordValidator('logIn');
passwordValidator('MyPass123');
passwordValidator('Pa$s$s');
