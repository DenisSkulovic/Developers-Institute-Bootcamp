//1
const numbers = [5,0,9,1,7,4,2,6,3,8];
let copy_numbers = numbers.slice();
copy_numbers = copy_numbers.toString();
console.log(copy_numbers);
console.log(typeof copy_numbers[0]);

//2
let string = numbers.join("- ");
console.log(string);

//3 bonus UNFINISHED (use nested loop)
// let num_array = [6,4,5,3,2,1,8,7,9,0];
// num_array