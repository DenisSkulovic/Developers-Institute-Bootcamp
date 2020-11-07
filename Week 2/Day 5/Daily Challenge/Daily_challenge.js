let input = prompt("Choose a number of beers");
let beers = parseInt(input);

for (let i = 1; beers > i; i++) {
    let str = (beers + " bottles of beer on the wall\n" + beers + " bottles of beer\nTake " + i + " down, pass it around\n" + (beers - i) + " bottles of beer on the wall");
    console.log(str)
    beers -= i;
}