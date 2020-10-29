// Remove Banana

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

function remove_word1(given_array, word) {
    let word_index = given_array.indexOf(word);
    if (word_index != -1) {
        given_array.splice(word_index, 1);
    }
}

remove_word1(fruits, "Banana");
console.log(fruits);

// or 

fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log(fruits);


// Sort array in order
fruits.sort();
console.log(fruits);


// Put "Kiwi" at the end of the array
fruits.push('Kiwi');
console.log(fruits);

//Remove "Apples" from the array with a different function
function remove_word2 (some_array, rem_word) {
    let new_array = [];
    for (word of some_array) {
        if (word != rem_word) {
            new_array.push(word);
        }
    }
    return new_array;
}
fruits = remove_word2(fruits, 'Apples');
console.log(fruits);

// Reverse the current array
function reverse_array(some_array) {
    let arr_len = some_array.length;
    let reversed_array =[];
    for (i=arr_len-1; i!=-1; i--) {
        reversed_array.push(some_array[i]);
    }
    return reversed_array;
}

fruits = reverse_array(fruits);
console.log(fruits)


// Access item "Oranges"
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);