// Exercise 1: Simple If/Else Statement
function bigger(var1, var2){
    if (var1 > var2){
        console.log("x is the biggest number");
    } else if (var1 < var2){
        console.log("y is the biggest number");
    } else {
        console.log("x and y are equal");
    }
}

let x, y;
x = 5;
y = 2;
bigger(x, y);


// Exercise 2: Chihuahua
let newDog = 'Chihuahua';

let str_len = newDog.length;
console.log("Length of newDog is", str_len);

console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog == 'Chihuahua'){
    console.log("I love Chihuahua, it's my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}


// Exercise 3: Even Or Not Even
let input_var = prompt('Please enter a number: ', 0);

if (input_var%2==0) {
    console.log(input_var + " is an even number");
} else {
    console.log(input_var + " is not an even number");
}


// Exercise 4: Group Chat
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

let array_len = users.length;

if (array_len < 1) {
    console.log('no one is online');
} else if (array_len == 1) {
    console.log(users[0] + ' is online');
} else if (array_len == 2) {
    console.log(users[0] + ' and ' + users[1] + ' are online');
} else if (array_len >= 3) {
    let remaining = array_len-2;
    console.log(users[0] + ', ' + users[1] + ' and ' + remaining + ' more are online');
}
