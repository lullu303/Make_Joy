function changeIcon(data) {
    let weather = data.weather[0].icon;

    HTML.classList.remove(...html.classList);
    descriptionIcon.classList.remove(...descriptionIcon.classList);
}

if(weather === 'Clouds') {
    html.classList.add('weather-clouds');
    descriptionIcon.classList.add('fas', 'fa-cloud-sun');
} else if (weather === 'Clear') {
    html.classList.add('weather-clear');
    descriptionIcon.classList.add('fas', 'fa-sun');
} else if (weather === 'Thunderstorm') {
    html.classList.add('weather-thunderstorm');
    descriptionIcon.classList.add('fas', 'fa-water');
} else if (weather === 'Rain') {
    html.classList.add('weather-rain');
    descriptionIcon.classList.add('fas', 'fa-unbrella');
} else if (weather == 'Snow') {
    html.classList.add('weather-snow');
    descriptionIcon.classList.add('fas', 'fa-snowflake');
} else if (weather === 'Atmosphere') {
    html.classList.add('weather-clouds');
    descriptionIcon.classList.add('fas', 'fa-smog');
} else {
    html.classList.add('weather-default');
    descriptionIcon.classList.add('fas', 'fa-cloud');
}