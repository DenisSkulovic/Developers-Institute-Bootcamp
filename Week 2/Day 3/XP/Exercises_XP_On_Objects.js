// Exercise 1: Attendance

let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
}

let student_name = prompt("What is your name?");

if ( !(student_name in guestList) ) {
    console.log('Hi! I am a guest.');
} else {
    let student_country = guestList[student_name];
    console.log('Hi! I\'m ' + student_name + ', and I\'m from ' + student_country);
}


// Exercise 2: Family
let family = {
    last_name: 'Lastname',
    size: 4,
    city: 'Karaganda',
    country: 'Kazakhstan'
}

console.log(Object.keys(family));
console.log(Object.values(family));


// Exercise 3: Building Management
let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}
//1
console.log(building['number_levels']);
//2
console.log(building['number_of_apt_by_level']['1']);
console.log(building['number_of_apt_by_level']['3']);
//3
let second_tenant = building['name_of_tenants']["2"];
console.log(second_tenant);
console.log(building['number_of_rooms_and_rent'][second_tenant][0]);
//4
let sarah_rent = building['number_of_rooms_and_rent']['Sarah'][1];
let david_rent = building['number_of_rooms_and_rent']['David'][1];
let dan_rent = building['number_of_rooms_and_rent']['Dan'][1];

if ( (sarah_rent+david_rent>dan_rent) ) {
    let new_amount = prompt('Please enter a new amount for Dan\'s rent: ');
    building['number_of_rooms_and_rent']['Dan'][2] = new_amount;
}

// Exercise 4: Checking The BMI
function bmi(m, h) {
    return (m/(h*h))
}
let person1 = {
    fullName:'Namy Surnameson',
    mass:300,
    height: 57
}
let person2 = {
    fullName:'Names Surnamesberg',
    mass:285,
    height:60
}
person1['bmi']=bmi(person1.mass, person1.height)
person2['bmi']=bmi(person2.mass, person2.height)

function compare_bmi(obj1, obj2) {
    let bmi1 = obj1['bmi'];
    let bmi2 = obj2['bmi'];
    let largest_bmi;
    if (bmi1>bmi2) {
        console.log(obj1['fullName']);
    } else {
        console.log(obj2['fullName']);
    }
}
compare_bmi(person1, person2);
