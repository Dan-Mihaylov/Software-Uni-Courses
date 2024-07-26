function toggle() {
    const buttonElement = document.getElementsByClassName('button')[0];
    const extraElement = document.getElementById('extra');

    switch (buttonElement.textContent.toLowerCase()) {
       
        case 'more':
            buttonElement.textContent = 'Less';
            extraElement.style.display = 'block';
            break;
        
            case 'less':
            buttonElement.textContent = 'More';
            extraElement.style.display = 'none';
            break;
    }
}