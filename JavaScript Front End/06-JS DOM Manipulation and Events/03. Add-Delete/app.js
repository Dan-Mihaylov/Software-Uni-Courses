function addItem() {
    console.log('Works')
    const listItemsElement = document.getElementById('items');

    const newText = document.getElementById('newItemText').value;

    const newLiElement = document.createElement('li');
    const newLinkElement = document.createElement('a');

    newLiElement.textContent = newText;
    listItemsElement.appendChild(newLiElement);

    newLinkElement.setAttribute('href', '#');
    newLinkElement.textContent = '[Delete]';
    newLinkElement.addEventListener('click', deleteElement);

    newLiElement.appendChild(newLinkElement);

    function deleteElement(event) {
        this.parentNode.parentNode.removeChild(this.parentNode);
    }
    
}