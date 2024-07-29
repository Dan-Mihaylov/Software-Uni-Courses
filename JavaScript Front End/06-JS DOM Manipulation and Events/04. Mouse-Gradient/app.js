function attachGradientEvents() {
    const gradientElement = document.getElementById('gradient').addEventListener('mousemove', event=>{
        
        const resultElement = document.getElementById('result');

        const clientWidth = event.target.clientWidth;
        const offsetX = event.offsetX;

        const result = Math.trunc(offsetX / clientWidth * 100);
        resultElement.textContent = result + '%';
    })
}