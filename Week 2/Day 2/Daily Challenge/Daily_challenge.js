

let some_string = 'this string has "not" and "bad" inside';

function not_bad_inside(string) {
    let first_not, first_bad;
    first_not = string.search('not');
    first_bad = string.search('bad');

    if ( (first_not<first_bad)  &&  ((first_not>=0) && (first_bad>=0)) ) {
        some_string = some_string.replace( some_string.substring(first_not, first_bad+3), 'good');
        console.log(string);
    } else {
        console.log(string);
    }
}

not_bad_inside(some_string);
