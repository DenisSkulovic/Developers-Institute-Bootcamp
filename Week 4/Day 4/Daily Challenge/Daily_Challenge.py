# Daily Challenge : Solve The Matrix
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden 
# message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the 
# leftmost column, select only the alphanumeric characters and connect them, then he 
# replaces every group of symbols between two alphanumeric characters by a space.

# Using his technique, try to decode this matrix:

#     7 3
#     Tsi
#     h%x
#     i #
#     sM 
#     $a 
#     #t%
#     ir!


def neo(*args):
    import string
    import re

    # convert columns to rows
    num_of_cols = args[0].__len__()
    columns = []
    for i in range(num_of_cols):
        column = ''
        for arg in args:
            column += arg[i]
        columns.append(column)

    # concating the columns into one long string
    message = ''.join(columns)
    message = message.replace(" ", "")

    # replacing the non-alphanumeric characters with spaces
    cleaned_message = ''
    for char in message:
        if char not in (string.ascii_lowercase + string.ascii_uppercase + ''.join([chr(i) for i in range(48, 58)])):
            cleaned_message += ' '
        else: 
            cleaned_message += char

    # there can be multiple spaces in a row, so the words are extracted and concatinated with just one space
    return ' '.join(re.findall("\\b\w+\\b", cleaned_message))
    




print(neo("7 3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"))