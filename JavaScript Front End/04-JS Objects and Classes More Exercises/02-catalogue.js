function catalogue(productsArray) {
    const catalogue = {};

    productsArray.forEach(product=>{
        const group = product[0];

        if (!catalogue[group]) {
            catalogue[group] = [];
        }

        catalogue[group].push(product);
    })

    const sortedCatalogueKeys = Object
    .keys(catalogue)
    .sort((a, b) => a.localeCompare(b))
    .forEach(key => {
        console.log(`${key}`);
        catalogue[key]
        .sort((a, b)=> a.localeCompare(b))
        .forEach(el => {
            const [product, price] = el.split(' : ')
            console.log(`  ${product}: ${price}`);
        })
        
    });

}


catalogue(
    [
        'Appricot : 20.4',
        'Fridge : 1500',
        'TV : 1499',
        'Deodorant : 10',
        'Boiler : 300',
        'Apple : 1.25',
        'Anti-Bug Spray : 15',
        'T-Shirt : 10'
        ]
);


catalogue(
    [
        'Omlet : 5.4',
        'Shirt : 15',
        'Cake : 59'
        ]
);