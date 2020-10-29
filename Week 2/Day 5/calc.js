// here we get the current value of the display
let calcDisplay = document.getElementById(display);

// console.log(calcDisplay.innerHTML);


let calcstr = "";

// function to compile the string for evaluation
function my_f(btn) {
    calcstr = calcstr + btn;

    // display the string on display
    calcDisplay.innerHTML = calcstr;
}

// function that calculates
function result() {
    let calcresult = eval(calcstr);
    // displays the result on the page
    calcDisplay.innerHTML = calcresult;
}

function remove () {
    if (calcDisplay.length > 0) {
        calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0,-1);
    }
    calcDisplay.innerHTML(calcstr);
}

function reset () {
    calcstr= "";
    calcDisplay.innerHTML = 0;
}