function lockedProfile() {
    const userCardEl = document.querySelector('.profile');
    const mainEl = document.getElementById('main');
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/profiles';
    
    async function loadProfiles(){
        
        try {
            const response = await fetch(baseUrl);
            const responseJson = await response.json();
            const responseDataValues = Object.values(responseJson);
            
            responseDataValues.forEach(data => {
                createProfile(data);
            })
            userCardEl.remove();
        } catch (error) {
            console.log(error);
            console.error('Error occurred: ', error);
        }
        
    }
    
    function createProfile(profileData) {
        const userCloneEl = userCardEl.cloneNode(true);
        
        const hiddenDivEl = userCloneEl.querySelector('div.user1Username');
        hiddenDivEl.className = 'hiddenInfo';
        
        const [lockedEl, unlockedEl] = userCloneEl.querySelectorAll('input[type="radio"]');
        lockedEl.name = profileData._id;
        unlockedEl.name = profileData._id;
        
        const usernameEl = userCloneEl.querySelector('input[type="text"]');
        usernameEl.value = profileData.username;
        
        const [emailEl, ageEl] = userCloneEl.querySelectorAll('input[type="email"]');
        emailEl.value = profileData.email;
        ageEl.value = profileData.age;
        
        const buttonEl = userCloneEl.querySelector('button');
        buttonEl.addEventListener('click', (e) => toggleInfo(e, lockedEl, hiddenDivEl));
        
        mainEl.append(userCloneEl);
    }
    
    function toggleInfo(event, lockedEl, hiddenDivEl) {
        cd  
        if (lockedEl.checked) {
            return;
        }
        
        const buttonElText = event.target.textContent;
        
        buttonElText === 'Show more' ? hiddenDivEl.className = 'user1Username' : hiddenDivEl.className = 'hiddenInfo';
        buttonElText === 'Show more' ? event.target.textContent = 'Hide it' : event.target.textContent = 'Show more';
    }
    
    loadProfiles();
    
}
