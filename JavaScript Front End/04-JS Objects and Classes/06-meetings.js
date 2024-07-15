function meetings(meetingsInfoArray){
    const meetingsMapped = meetingsInfoArray.map(el => el.split(' '));
    const schedule = new Object();

    for (const item of meetingsMapped) {
        const day = item[0];
        const person = item[1];

        if (schedule.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            schedule[day] = person;
            console.log(`Scheduled for ${day}`)
        };
    };

    for ([day, person] of Object.entries(schedule)) {
        console.log(`${day} -> ${person}`);
    };

};


meetings(['Monday Peter','Wednesday Bill','Monday Tim','Friday Tim']);
