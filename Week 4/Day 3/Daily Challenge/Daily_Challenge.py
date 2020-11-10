# Daily Challenge: Caesar Cypher
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of
# positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, the user entries the program,
# and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# More information on caesar cipher is available on internet.


def caesars_cypher(message, shift, encrypt='encrypt'):
    shift = int(shift)

    capital_letters = []
    for i in range(65, 91):
        capital_letters.append(chr(i))
    triple_capital_letters = capital_letters + capital_letters + capital_letters

    lower_letters = []
    for i in range(97, 123):
        lower_letters.append(chr(i))
    triple_lower_letters = lower_letters + lower_letters + lower_letters

    alphabet_len = capital_letters.__len__()

    if encrypt != 'encrypt':
        shift = shift*(-1)

    changed_message = ''
    for char in message:
        if char not in capital_letters + lower_letters:
            changed_message += char
        # if upper case
        elif char in capital_letters:
            letter_ind = capital_letters.index(char)
            changed_message += triple_capital_letters[alphabet_len +
                                                letter_ind + shift]
        # if lower case
        elif char in lower_letters:
            letter_ind = lower_letters.index(char)
            changed_message += triple_lower_letters[alphabet_len +
                                              letter_ind + shift]
    return changed_message


message = input("What is your message: ")
step = input("What is the step of the cypher: ")
action = input("Do you want to 'encrypt' or 'decypher': ")

print(caesars_cypher(message, step, action))
