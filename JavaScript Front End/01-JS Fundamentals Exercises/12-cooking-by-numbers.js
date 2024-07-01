function cook(...args) {
    let number = args.shift();

    const actions = {
        'chop': (num) => num / 2,
        'dice': (num) => Math.sqrt(num),
        'spice': (num) => num + 1,
        'bake': (num) => num * 3,
        'fillet': (num) => num * 0.8
    };

    for (arg of args) {
        number = actions[arg](number);
        console.log(number);
    };
};


cook('32', 'chop', 'chop', 'chop', 'chop', 'chop');
cook('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
