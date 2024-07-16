function solve(input){

    class Song{
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }

    }

    const songsByType = new Object();
    const playlist = new Array();

    const songItems = input.shift();
    const lookForType = input.pop();

    for (let i = 0; i < songItems; i++) {
        let songType;
        let songName;
        let songTime;

        [songType, songName, songTime] = input[i].split('_');
        const song = new Song(songType, songName, songTime);
        playlist.push(song)
        
        if (!songsByType[songType]) {
            songsByType[songType] = [];
        }

        songsByType[songType].push(song);
    }

    if (lookForType === 'all') {
        playlist.forEach(song => {
            console.log(song.name);
        });
    } else {
        songsByType[lookForType].forEach(song => {
            console.log(song.name);
        })
    }

}


solve([3,
        'favourite_DownTown_3:14',
        'favourite_Kiss_4:16',
        'favourite_Smooth Criminal_4:01',
        'favourite']);

solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']);


