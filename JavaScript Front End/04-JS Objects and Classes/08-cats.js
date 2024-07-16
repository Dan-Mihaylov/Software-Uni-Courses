function cats(catsArray){
    
    class Cat{
        constructor(name, age){
            this.name = name;
            this.age = age;
        };

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        };
    };

    const catObjects = new Array();

    for (const catInfo of catsArray) {
        let catName;
        let catAge;

        [catName, catAge] = catInfo.split(' ');
        catObjects.push(new Cat(catName, catAge));
    };

    for (const cat of catObjects) {
        cat.meow();
    };
};

cats(['Mellow 2', 'Tom 5']);
cats(['Candy 1', 'Poppy 3', 'Nyx 2']);

