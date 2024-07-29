function deleteByEmail() {
    const resultElement = document.getElementById('result');
    const lookForEmail = document.querySelector('input[name="email"]').value;
    const foundRowElement = Array.from(document.querySelectorAll('tbody tr'))
    .filter(row => row.children[1].textContent == lookForEmail);

    if (!foundRowElement.length > 0) {
        resultElement.textContent = 'Not found.';
    } else {
        foundRowElement[0].parentNode.removeChild(foundRowElement[0])
        resultElement.textContent = 'Deleted';
    }

    console.log(foundRowElement);
}