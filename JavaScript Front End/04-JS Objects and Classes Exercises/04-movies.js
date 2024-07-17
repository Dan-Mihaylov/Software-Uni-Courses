function movies(moviesArray){
    const moviesList = new Array();
    
    function findMovie(lookForName){
        for (const movie of moviesList) {
            if (movie.name == lookForName) {
                return movie;
            }
        }
        return false;
    }
    
    for (let command of moviesArray){
        if (command.includes('addMovie')) {
            movieNameArray = command.split('addMovie ');
            moviesList.push(
                new Object({name: movieNameArray.pop()})
            )
        } else if (command.includes('directedBy')){
            let movieName;
            let director;
            
            [movieName, director] = command.split(' directedBy ');
            // check if movie in and if in add director.
            const foundMovie = findMovie(movieName);
            if (foundMovie) {
                foundMovie['director'] = director;
            }
        } else if (command.includes('onDate')) {
            let movieName;
            let date;
            
            [movieName, date] = command.split(' onDate ');
            const foundMovie = findMovie(movieName);
            if (foundMovie){
                foundMovie['date'] = date;
            }
        }
    }
    
    moviesList.forEach(movie => {
        if (movie.director && movie.date){
        console.log(JSON.stringify(movie));
        }
    })
}


movies(
    [
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
);


movies(
    [
        'addMovie The Avengers',
        'addMovie Superman',
        'The Avengers directedBy Anthony Russo',
        'The Avengers onDate 30.07.2010',
        'Captain America onDate 30.07.2010',
        'Captain America directedBy Joe Russo'
    ]
);