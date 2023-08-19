
const txt1 = document.getElementById('username_input');
const btn1 = document.getElementById('get_username_btn');
const output1 = document.getElementById('output_p');

function display_input() {
    output1.innerHTML = txt1.value;
    }



btn1.addEventListener('click',display_input);
