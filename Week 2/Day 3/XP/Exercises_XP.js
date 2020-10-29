// Exercise 1: Your Favorite Colors

let colors = ['red','blue','green','yellow','orange','white','purple','sky','chocolate','brown','magenta','black','cream'];
let suffix = ['st','nd','rd','th'];
for (i=0; i<colors.length; i++) {
    
    let place = i+1;
    place = place.toString();
    let last_digit = place.slice(-1)
    let len = place.length;
    //teens
    if ((len==2) && (place[0]=='1')) {
        console.log('My ' + place + suffix[3] + ' choice is ' + colors[i])
    }
    //st
    else if (last_digit=='1') {
        console.log('My ' + place + suffix[0] + ' choice is ' + colors[i])
    }
    //nd
    else if (last_digit=='2') {
        console.log('My ' + place + suffix[1] + ' choice is ' + colors[i])
    }
    //rd
    else if (last_digit=='3') {
        console.log('My ' + place + suffix[2] + ' choice is ' + colors[i])
    }
    else {
        console.log('My ' + place + suffix[3] + ' choice is ' + colors[i])
    }
}

// Exercise 2: Secret Group
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let first_letters = [];
for (name of names) {
    let first_letter = name[0];
    first_letters.push(first_letter)
}
first_letters.sort();
let society_name = '';
for (letter of first_letters) {
    society_name += letter;
}
console.log(society_name);

// // Exercise 3: Repeat The Question
// let input = prompt("Please enter a number");
// while (input < 10) {
//     input = prompt("Please enter a number");
// }

// Exercise 4: List of People
//1
let people = ["Greg", "Mary", "Devon", "James"];
for (human of people) {
    console.log(human);
}
console.log(people);

//2
people.shift();
console.log(people);

//3
people.splice(-1);
people.push('Jason');

//4
people.push('Denis');
console.log(people);

//5
for (human of people) {
    console.log(human);
    if (human == 'Mary') {
        break;
    } else {continue;}
}

//6
let new_array = people.slice(1,-1);
console.log(new_array);

//7
console.log(people.indexOf('Mary'));

//8
console.log(people.indexOf('Foo'));

//9
let last = people[people.length-1];
console.log(last);


// Exercise 5: Divisible By Three
let nums = ['123','8409','100853','33333333','7'];
function odd_or_not(some_array) {
    for (num of some_array) {
        if (num%3==0) {
            console.log(true);
        } else {
            console.log(false);
        }
    }
}

odd_or_not(nums);

// Exercise 6: Playing with numbers
//1
let age = [20,5,12,43,98,55];
let sum = 0;
for (num of age) {
    sum += num;
}
console.log(sum);
//2
function max(some_array) {
    let current_largest;
    current_largest = some_array[0];
    for (num of some_array) {
        if (num > current_largest) {
            current_largest = num;
            continue;
        }
    }
    return current_largest;
}

console.log(max(age));
