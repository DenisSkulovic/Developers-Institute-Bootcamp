// Exercise 1: Keyless Car

function checkDriverAge(age) {
    if (Number(age) < 18) {
        alert("Sorry, you are too yound to drive this car. Powering off");
    } else if (Number(age) > 18) {
        alert("Powering On. Enjoy the ride!");
    } else if (Number(age) === 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
}


// Exercise 2: Is_Blank

function is_Blank(string) {
    if (string.length == 0) {
        return true;
    } else {
        return false;
    }
}


// Exercise 3: Abbrev_name

function abbrev_name(name) {
    let split_name = name.split(' ');
    let abb_name = split_name[0] + ' ' + split_name[1][0] + '.';
    return abb_name;
}

abbrev_name("Robin Singh")


// Exercise 4: SwapCase

function swapcase(string) {
    let new_string = '';
    for (letter of string) {
        if (letter === letter.toLowerCase()) {
            letter = letter.toUpperCase();
            new_string += letter;
        } else {
            letter = letter.toLowerCase();
            new_string += letter;
        }
    }
    return new_string;
}

console.log(swapcase("SpOnGeBoB"));


// Exercise 5: Amazon Shopping
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket() {
    let request = prompt("What item do you want?");
    request = request.toLowerCase();
    if (amazonBasket.contains(request)) {
        console.log("The item is in the basket.");
    } else {
        console.log("The item is not in the basket.");
    }
}


// Exercise 6: What's In My Wallet?

function changeEnough(wallet_arr, due_amt) {
    let q = 0.25;
    let d = 0.10;
    let n = 0.5;
    let p = 0.1;

    let wallet_value = wallet_arr[0] * q + wallet_arr[1] * d + wallet_arr[2] * n + wallet_arr[3] * p
    if (wallet_value >= due_amt) {
        return true;
    } else {
        return false;
    }
}


// Exercise 7: Shopping List
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ["banana", "orange", "apple"]

function myBill() {
    let cost = 0;

    for (item of shoppingList) {
        if (stock[item] > 0) {
            cost += prices[item];
            stock[item] -= 1;
        }
    }

    return cost;
}

console.log(myBill());


// Exercise 8: Find The Multiples Of 23

function multiples23() {
    let multiples = [];
    for (let i = 0; i < 500; i++) {
        if (i % 23 == 0) {
            multiples = multiples.concat([i]);
        }
    }

    let sum = 0;
    for (num of multiples) {
        sum += num;
    }
    return sum;
}

console.log(multiples23());


// Exercise 9: Omnipresent Value
function isOmnipresent(arr, val) {
    let arr_len = arr.length;
    let presence_count = 0;
    for (let i = 0; i < arr_len; i++) {
        if (arr[i].includes(val)) {
            presence_count += 1;
        }
    }

    if (arr_len == presence_count) {
        return true;
    } else {
        return false;
    }
}

console.log(isOmnipresent([
    [1, 1],
    [1, 3],
    [5, 1],
    [6, 1]
], 6))


// Exercise 10: Vacations Costs
// 1
function hotel_cost() {
    let nights_num = prompt(" How many nights would you like to stay?");
    let reg = /\b\d+\b/;
    if (!reg.test(nights_num)) {
        alert("Please enter a valid number of nights.");
    }
    return 140 * nights_num;
}

//2
function plane_ride_cost() {
    let dest = prompt("What is your destination?");
    let reg = /\d+/;
    if (dest == "London") {
        return "$183";
    } else if (dest == "Paris") {
        return "$220";
    } else if ((reg.test(dest)) || dest.length == 0) {
        alert("Please enter a valid destination.");
    } else {
        return "$300";
    }
}

//3
function rental_car_cost() {
    let input = prompt("Please enter the number of days: ");
    let reg = /\d+/;
    if (!reg.test(input) || (input.length == 0)) {
        alert("Please enter a valid number.");
    }
    if (input > 10) {
        return input * 0.95 * 40;
    } else {
        return input * 40;
    }
}

//4
function total_vacation_cost() {
    let hotelCost = hotel_cost();
    let planeRideCost = plane_ride_cost();
    let rentalCarCost = rental_car_cost();
    return hotelCost + planeRideCost + rentalCarCost
}

//5
total_vacation_cost()