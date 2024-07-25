function extractText() {
    const resultArea = document.getElementById('result');
    const elementId = 'items';
    const items = Array.from(document.getElementById(elementId).children).map((el)=> el.textContent);
    resultArea.textContent = items.join('\n');
}