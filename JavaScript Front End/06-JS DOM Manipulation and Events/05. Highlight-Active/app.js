function focused() {
    document.querySelectorAll('input[type="text"]').forEach(el=>{
        el.addEventListener('focus', getFocus);
        el.addEventListener('blur', getBlur);
    })

    function getFocus(event) {
        event.currentTarget.parentNode.className = 'focused';
    }

    function getBlur(event) { 
        event.currentTarget.parentNode.className = '';
    }
}