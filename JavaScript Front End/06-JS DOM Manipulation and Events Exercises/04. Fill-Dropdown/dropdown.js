function addItem() {
    const textElement = document.getElementById('newItemText');
    const valueElement = document.getElementById('newItemValue');
    const menuElement = document.getElementById('menu');

    if (textElement.value.trim() == '' || valueElement.value.trim() == '') {
        return;
    }

    const newOptionElement = document.createElement('option');
    newOptionElement.value = valueElement.value;
    newOptionElement.textContent = textElement.value;
    
    menuElement.append(newOptionElement);

    textElement.value = '';
    valueElement.value = '';
}