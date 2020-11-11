# Exercise 1 : What’s Your Name ?
# Write a function called get_full_name() that receives three arguments:
# a first_name, a middle_name and a last_name.
# But the middle_name should be optional, if it’s omitted by the user, the
# name returned will only contain the first and the last name.
# get_full_name(first_name="john", middle_name="hooker", last_name="lee")
# will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

# def get_full_name(first_name, last_name, middle_name=''):
#     if middle_name.__len__() == 0:
#         result = first_name + " " + last_name
#     else:
#         result = first_name + " " + middle_name + " " + last_name
#     return result

# print(get_full_name(first_name="John", middle_name = "Lee", last_name="Hooker"))



# Exercise 2 : Box Of Stars
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

# def box_printer(*args):
#     longest_word_len = 0
#     for word in args:
#         if word.__len__() > longest_word_len:
#             longest_word_len = word.__len__()
#     def stars(x): return x*"*"
#     def word_stars(word, spaces_len): return "* " + \
#         word + spaces_len*' ' + " *"
#     print(stars(longest_word_len+4))
#     for word in args:
#         spaces_len = longest_word_len - word.__len__()
#         starred_word = word_stars(word, spaces_len)
#         print(starred_word)
#     print(stars(longest_word_len+4))

# box_printer("test", 'sentence', 'this', 'is', 'a', 'word')




# Exercise 3
# Analyse this code before executing it. Write some comments next to each line and find the output.
# What is the purpose of it ?
# def insertion_sort(alist):
#    for index in range(1,len(alist)):
#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1
#          print(alist)

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)





# Exercise 4 : From English To Morse
# Write a function that converts English text to Morse code and another one that does 
# the opposite.
# Hint: Check on internet for translation table, every letter is separated with a 
# space and every word is separated with a slash /.
def words_to_morse(text):
    LETTER_TO_MORSE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
    text = text.upper()
    morse = []
    for char in text:
        if char == " ":
            morse += ['/']
        elif char not in LETTER_TO_MORSE_DICT.keys():
            pass
        else:
            morse += [LETTER_TO_MORSE_DICT[char]]
    return ' '.join(morse)


def morse_to_words(morse):
    LETTER_TO_MORSE_DICT = { 'A':'.-', 'B':'-...', 
                        'C':'-.-.', 'D':'-..', 'E':'.', 
                        'F':'..-.', 'G':'--.', 'H':'....', 
                        'I':'..', 'J':'.---', 'K':'-.-', 
                        'L':'.-..', 'M':'--', 'N':'-.', 
                        'O':'---', 'P':'.--.', 'Q':'--.-', 
                        'R':'.-.', 'S':'...', 'T':'-', 
                        'U':'..-', 'V':'...-', 'W':'.--', 
                        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                        '1':'.----', '2':'..---', '3':'...--', 
                        '4':'....-', '5':'.....', '6':'-....', 
                        '7':'--...', '8':'---..', '9':'----.', 
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                        '?':'..--..', '/':'-..-.', '-':'-....-', 
                        '(':'-.--.', ')':'-.--.-'}
    MORSE_TO_LETTER_DICT = dict(zip(LETTER_TO_MORSE_DICT.values(), LETTER_TO_MORSE_DICT.keys()))
    
    morse_words = morse.split('/')
    text = ''
    for morse_word in morse_words:
        morse_letters = morse_word.split(' ')
        word = ''
        for morse_letter in morse_letters:
            if morse_letter.__len__() > 0:
                word += MORSE_TO_LETTER_DICT[morse_letter]
        text += word+' '
    return text

print(words_to_morse("Test text with numbers 1 2 3 and some symbols ( ) / ?"))
print(morse_to_words(words_to_morse("Test text with numbers 1 2 3 and some symbols ( ) / ?")))

