function solve(arr) {
    let encryptedSpell = arr[0];
    const commands = arr.slice(1, arr.length - 1);

    commands.forEach(command => {
        const data = command.split('!');

        switch (data[0]) {
            case 'RemoveEven':
                removeEven();
                break;
            case 'TakePart':
                takePart(Number(data[1]), Number(data[2]));
                break;
            case 'Reverse':
                reverseSubstring(data[1]);
        }
    });

    function removeEven() {
        let temp = '';
        
        for (let i = 0; i < encryptedSpell.length; i++) {
            if (i % 2 == 0) {
                temp += encryptedSpell[i];
            }
        };

        encryptedSpell = temp;
        console.log(encryptedSpell);
    }

    function takePart(startIndex, endIndex) {
        let temp = encryptedSpell.slice(startIndex, endIndex);
        encryptedSpell = temp;
        console.log(encryptedSpell);
    }

    function reverseSubstring(substring) {
        if (encryptedSpell.includes(substring)) {
            encryptedSpell = encryptedSpell.replace(substring, '');
            const reversedSubstring = substring.split('').reverse().join('');
            encryptedSpell += reversedSubstring;
            console.log(encryptedSpell);
        } else {
            console.log('Error');
        }
    }

    console.log(`The concealed spell is: ${encryptedSpell}`);

}


solve(["hZwemtroiui5tfone1haGnanbvcaploL2u2a2n2i2m", 
    "TakePart!31!42",
    "RemoveEven",
    "Reverse!anim",
    "Reverse!sad",
    "End"]);
