function attachEvents() {
    const imageMap = {
        'Sunny': '&#x2600',
        'Partly sunny': '&#x26C5',
        'Overcast': '&#x2601',
        'Rain': '&#x2614',
        'Degrees': '&#176' 
    }
    
    const getWeatherButtonElement = document.getElementById('submit');
    getWeatherButtonElement.addEventListener('click', displayWeather);

    const baseLocationUrl = 'http://localhost:3030/jsonstore/forecaster/locations';
    const baseCurrUrl = 'http://localhost:3030/jsonstore/forecaster/today/';
    const baseUpcomingUrl = 'http://localhost:3030/jsonstore/forecaster/upcoming/';

    const locationInputElement = document.getElementById('location');
    const forecastElement = document.getElementById('forecast');
    const currentWeatherElement = document.getElementById('current');
    const upcomingWeatherElement = document.getElementById('upcoming');

    function displayWeather(event) {
        const locationName = locationInputElement.value;
        forecastElement.style.display = 'block';
        clearForecastElements();

        fetch(baseLocationUrl)
            .then(response => response.json())
            .then(dataArray => {
                const location = dataArray.filter(
                    (obj) => obj.name == locationName || obj.code == locationName
                )[0];

                if (!location) {
                    throw new Error('No results')
                }

                fillCurrentWeather(location);
                fillUpcomingWeather(location);
            })
            .catch(error => {
                forecastElement.textContent = 'Error';
            });
    }

    function fillCurrentWeather(locationObject) {
        const locationCode = locationObject.code;

        fetch(baseCurrUrl + locationCode)
            .then(response => response.json())
            .then(data => {
                if (!data){
                    throw Error('No data')
                }
                createCurrentWeatherElements(data);
            })
            .catch(error => console.log(error))
    }

    function fillUpcomingWeather(locationObject){
        const locationCode = locationObject.code;
        
        fetch(baseUpcomingUrl + locationCode)
            .then(response => response.json())
            .then(data => {
                const forecastData = data.forecast;
                if(!forecastData) {
                    throw Error('No data')
                }
                createUpcomingWeatherElements(forecastData);
            })
            .catch(error => console.log(error))
    }

    function createUpcomingWeatherElements(forecastData) {
        const forecastInfoDivEl = document.createElement('div');
        forecastInfoDivEl.className = 'forecast-info';
        upcomingWeatherElement.append(forecastInfoDivEl);

        [...forecastData].forEach(forecast => {
            const upcomingSpanEl = document.createElement('span');
            upcomingSpanEl.className = 'upcoming';
            forecastInfoDivEl.append(upcomingSpanEl);

            const symbolSpanEl = document.createElement('span');
            symbolSpanEl.className = 'symbol';
            symbolSpanEl.innerHTML = imageMap[forecast.condition];
            upcomingSpanEl.append(symbolSpanEl);

            const degreesSpanEl = document.createElement('span');
            degreesSpanEl.className = 'forecast-data';
            degreesSpanEl.innerHTML = `${forecast.low}${imageMap['Degrees']}/${forecast.high}${imageMap['Degrees']}`;
            upcomingSpanEl.append(degreesSpanEl);

            const conditionSpanEl = document.createElement('span');
            conditionSpanEl.className = 'forecast-data';
            conditionSpanEl.innerHTML = forecast.condition;
            upcomingSpanEl.append(conditionSpanEl);

        })
    }

    function createCurrentWeatherElements(forecastData) {
        const forecastDivElement = document.createElement('div');
        forecastDivElement.className = 'forecasts';
        currentWeatherElement.append(forecastDivElement);

        const spanConditionSymbolEl = document.createElement('span');
        spanConditionSymbolEl.className = 'condition symbol';
        spanConditionSymbolEl.innerHTML = imageMap[forecastData.forecast.condition];
        forecastDivElement.append(spanConditionSymbolEl);

        const spanConditionEl = document.createElement('span');
        spanConditionEl.className = 'condition';
        forecastDivElement.append(spanConditionEl);

        const firstDataSpanEl = document.createElement('span');
        firstDataSpanEl.className = 'forecast-data';
        firstDataSpanEl.textContent = forecastData.name;
        spanConditionEl.append(firstDataSpanEl);

        const secondDataSpanEl = document.createElement('span');
        secondDataSpanEl.className = 'forecast-data';
        secondDataSpanEl.innerHTML = `${forecastData.forecast.low}${imageMap['Degrees']}/${forecastData.forecast.high}${imageMap['Degrees']}`;
        spanConditionEl.append(secondDataSpanEl);

        const thirdDataSpanEl = document.createElement('span');
        thirdDataSpanEl.className = 'forecast-data';
        thirdDataSpanEl.textContent = forecastData.forecast.condition;
        spanConditionEl.append(thirdDataSpanEl);

    }


    function clearForecastElements(){
        [...forecastElement.children].forEach(child => {
            if (child.children[1]){
                child.children[1].remove();
            }
        })
    }


}

attachEvents();
