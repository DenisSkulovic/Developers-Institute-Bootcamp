let solar = document.querySelector("body")

let planets = ["Earth", "Jupiter", "Mars", "Neptune", "Saturn", "Venus", "Mercury", "Uranus"];

function randn(min, max) {
    let num = Math.random() * (max - min) + min;
    return Math.round(num);
}

for (planet of planets) {
    let new_elem = document.createElement('div');
    new_elem.setAttribute("class", "planet");
    new_elem.innerText = planet;
    new_elem.style.backgroundColor = "rgb(" + randn(100, 255) + "," + randn(100, 255) + "," + randn(100, 255) + ")";
    solar.appendChild(new_elem);
}