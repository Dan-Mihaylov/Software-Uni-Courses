function addItem() {
    const listElement = document.getElementById('items');
    const newText = document.getElementById('newItemText').value;

    const newLiElement = document.createElement('li');
    newLiElement.textContent = newText;

    listElement.appendChild(newLiElement);
}