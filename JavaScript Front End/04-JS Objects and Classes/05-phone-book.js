function phoneBook(phonesArray){
    const phoneCatalog = {};

    for (const info of phonesArray){
        let personName;
        let personPhone;

        [personName, personPhone]= info.split(' ');
        phoneCatalog[personName] = personPhone;
    };

    for (let key in phoneCatalog){
        console.log(`${key} -> ${phoneCatalog[key]}`);
    };
};

phoneBook(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']);

phoneBook(['George 0552554',
    'Peter 087587',
    'George 0453112',
    'Bill 0845344']);

