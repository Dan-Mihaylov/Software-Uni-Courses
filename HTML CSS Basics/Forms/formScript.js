document.getElementById('confirm_button').addEventListener('click', function () {
            const checkboxes = document.getElementsByName('vehicle');
            const selectedVehicles = [];

            checkboxes.forEach(function (checkbox) {
                if (checkbox.checked) {
                    selectedVehicles.push(checkbox.value);
                }
            });

            const resultParagraph = document.getElementById('result_paragraph');
            const resultHeader = document.getElementById('result_header');
            const resultDiv = document.getElementById('result-div');

            if (selectedVehicles.length > 0) {
                resultDiv.style.opacity= 1;
                resultHeader.textContent = "Result";
                resultParagraph.textContent = 'You have selected: ' + selectedVehicles.join(', ') + ' vehicles.';
            } else {
                resultDiv.style.opacity = 1;
                resultHeader.textContent = "Result";
                resultParagraph.textContent = 'You need to select at least one vehicle.';
            }
        });

        document.getElementById('clear_button').addEventListener('click', function () {
            const result_div = document.getElementById('result-div')
            result_div.style.opacity = 0;
        });


document.addEventListener('DOMContentLoaded', function() {
    const confirmButton = document.getElementById('confirm-selection-btn');
    const displayResult = document.getElementById('display-radio-res');

    confirmButton.addEventListener('click', function(event) {
        event.preventDefault();

        const selectedRadio = document.querySelector('.radio:checked');
        const radioResult = document.getElementById('radio-result');

        if (selectedRadio.title === "correct") {
            radioResult.style.opacity = 1;
            displayResult.innerHTML = `You have selected: ${selectedRadio.value}<br>
            Your answer is <b style="color:green;">Correct</b>!`;
        } else if (selectedRadio.title !== "correct") {
            radioResult.style.opacity = 1;
            displayResult.innerHTML = `You have selected: ${selectedRadio.value}<br>
            Your answer is <b style="color:darkred;">Wrong</b>!`;
        } else {
            radioResult.style.opacity = 1;
            displayResult.textContent = 'Please select an answer.';
        }
    });
});

    document.getElementById('clear-radio').addEventListener('click', function () {
        const result_div = document.getElementById('radio-result');
        const resultText = document.getElementById('display-radio-res');
        const radioInputs = document.querySelectorAll('.radio');
        result_div.style.opacity = 0;
        resultText.textContent = ''

        radioInputs.forEach(function(radio) {
            radio.checked = false;
        });

    });
