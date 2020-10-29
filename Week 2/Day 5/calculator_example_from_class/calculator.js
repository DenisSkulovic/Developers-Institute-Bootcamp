let calcDisplay = document.getElementById("display");
// console.log(calcDisplay.innerHTML);

// btn for button

let calcstring="";

function my_f(btn){
	calcstring=calcstring + btn;
	calcDisplay.innerHTML= calcstring;
	// console.log(calcDisplay)
}

function result(){
	let calcresult = eval(calcstring)
	calcDisplay.innerHTML=calcresult
	// console.log(calcresult)

}

function cero(){
	calcstring = 0
	let cero = (calcstring);
	calcDisplay.innerHTML=cero

}

function remove(){
	if (calcDisplay.innerHTML.length>1) {
		calcDisplay.innerHTML= calcDisplay.innerHTML.slice(0,-1)
	}else{
		calcDisplay.innerHTML= 0
	}
	calcDisplay.innerHTML
}