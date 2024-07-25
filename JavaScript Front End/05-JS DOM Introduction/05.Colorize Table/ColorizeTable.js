function colorize() {
    const elements = Array.from(document.querySelectorAll('table tr:nth-child(even)')).map((el) => el.style.backgroundColor='teal');
}