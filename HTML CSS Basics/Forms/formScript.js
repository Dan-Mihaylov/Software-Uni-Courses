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

