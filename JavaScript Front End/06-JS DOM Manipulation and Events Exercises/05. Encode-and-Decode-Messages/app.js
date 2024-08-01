function encodeAndDecodeMessages() {
    
    const [encodeButtonElement, decodeButtonElement] = document.querySelectorAll('div button');
    
    encodeButtonElement.addEventListener('click', encodeText);
    decodeButtonElement.addEventListener('click', decodeText);
    
    function encodeText(event) {
        const resultTextareaElement = document.querySelector('div:nth-child(2) textarea');
        const textareaElement = event.target.parentNode.querySelector('textarea');

        const encodedText = textareaElement
          .value
          .split('')
          .map((char) => String.fromCharCode(char.charCodeAt() + 1))
          .join('');

        resultTextareaElement.value = encodedText;
        textareaElement.value = '';
    }
    
    function decodeText(event) {
        const textareaElement = event.target.parentNode.querySelector('textarea');

        const decodedText = textareaElement
            .value
            .split('')
            .map((char) => String.fromCharCode(char.charCodeAt() - 1))
            .join('');
        
        textareaElement.value = decodedText;
    }
    
}