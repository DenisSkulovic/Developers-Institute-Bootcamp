function hangman(secret_word) {
    secret_word = secret_word.toLowerCase();
    // splitting secret word to make an array of characters
    let secret_word_letters = Array.from(secret_word);
    // getting word length
    let secret_word_len = secret_word.length;
    // defining the "hidden" character
    let blank_val = "*";

    // compiling the initial word to display (e.g. ********)
    let display_str = '';
    for (char of secret_word_letters) {
        display_str = display_str + blank_val;
    }

    // regex pattern to later check if * are still present in the display_str
    let reg = /\*+/;
    // an array to record the history of inputs from user
    let input_history = []
    // initial number of tries
    let tries = 10;
    // won flag (0 for LOST and 1 for WIN)
    let victory = 0;

    // the main game loop. Loops until there are no * present in the display_str or out of tries
    while (((secret_word_len == 0) || (reg.test(display_str))) && (tries > 0)) {
        // collecting and storing input
        let input = prompt("Enter a letter");
        input = input.toLowerCase();

        // making sure input is valid
        if ((input.length != 1)) {
            alert("Entry is invalid. Try arain.")
            continue
        } else if (input_history.includes(input)) {
            alert("This letter has already been tried. Try another one.")
            continue
        }

        // recording inputs
        input_history = input_history.concat([input]);

        // compiling string to display
        display_str = '';
        for (char of secret_word_letters) {
            if ((input_history.includes(char))) {
                display_str = display_str + char;
            } else {
                display_str = display_str + blank_val;
            }
        }
        let tries_str = 'Tries remaining: ' + tries;
        console.log(display_str, tries_str);
        tries = tries - 1;
    }

    // deciding if won or lost (1 if no * are in the string)
    if (!(reg.test(display_str))) {
        victory = 1
    }

    // if there are still tries and victory=1, you are declared victorious
    if ((tries && victory) > 0) {
        alert('YOU WON');
    } else {
        alert('YOU LOST');
    }
}

hangman("developer");