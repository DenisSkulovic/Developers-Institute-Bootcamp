# Exercise 1: Birthday Look-Up
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message to the user. Then tell him: “You can look up the birthday of the people in the list!”
# Ask the user to give you a person’s name and store his answer in a variable.
# Get the birthday for the person’s name from the birthdays dictionary.
# Print out the birthday with a nicely-formatted message.

# birthday = {"Denis": "01-01-1899",
#             "Kevin": "06-01-1898",
#             "Kily": "02-03-1894",
#             "Lily": "10-10-1888",
#             "Olga": "04-04-1878"}

# inputName = input("Enter the person's name: ")
# print(f"The birthday is: {birthday[inputName]}")



# Exercise 2: Birthdays Advanced
# Before asking the user to type in a person’s name, print out all of the names from the dictionary, to make it easier for them to choose.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have birthday information for “”)

# for name in birthday.keys():
#     print(name)

# choise = input("Please choose a name: ")
# try:
#     print(birthday[choise])
# except:
#     print(f"Sorry, we don’t have birthday information for {choise}")



# Exercise 3: Add Your Own Birthday
# Insert this new code: before you offer the user to type a person’s name to look up, ask the user to add a birthday first:
# Ask the user for a person’s name – store it in a variable
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# The rest of your code should follow (from Exercise 2).
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

# userName = input("What is your name")
# userBirthday = input("What is your birthday")
# birthday[userName] = userBirthday

# for name in birthday.keys():
#     print(name)

# choise = input("Please choose a name: ")
# try:
#     print(birthday[choise])
# except:
#     print(f"Sorry, we don’t have birthday information for {choise}")



# Exercise 4: Fruit Shop:
# Create a new dictionary called items and add the following key-value pairs to it using code. They each represent an item and its price
    # "banana": 4,
    # "apple": 2,
    # "orange": 1.5,
    # "pear": 3
# Print all the items and their prices in your dictionary in a human-readable way
# Add stock information to each item (keep track of how many of each item our shop has).
# Once you’ve added stock info to the item, write some code to figure out how much it would cost to buy your entire stock of all items

# items = {"banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3}

# for fruit, price in items.items():
#     print(f"The price of {fruit} is {price}")

# for fruit, price in items.items():
#     items[fruit] = {"price": price,
#                     "quantity": 4}


# print(sum([priceQuantityPair["price"]*priceQuantityPair["quantity"] for priceQuantityPair in items.values()]))

# Exercise 4 : Cars
# Copy the following string into your script: “Volkswagen, Toyota, Ford Motor, Honda, Chevrolet”
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
# Print out the above information with meaningful output messages.
# Bonus: There are a few duplicates in this list [“Honda”,”Volkswagen”, “Toyota”, “Ford Motor”, “Honda”, “Chevrolet”, “Toyota”]:
# Remove these programmatically. (Hint: you can use sets to help you).
# Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), and also print out a message saying how many companies are now in the list.
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Kia"

array = string.split(", ")
# print(f"There are {array.__len__()} manufacturers")

# print(sorted(array, reverse=True))

import re
have_o = [car for car in array if re.match("\w*[Oo]+\w*", car)]
have_no_i = [car for car in array if re.match("\\b[^Ii]+\\b", car)]

print(f"{have_o.__len__()} have 'o' and {have_no_i.__len__()} have no 'i'")


no_duplicates = list(set(["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]))
print(no_duplicates)

no_duplicates_sorted = sorted(no_duplicates)

for company in no_duplicates_sorted:
    reversed = ''
    for char in company[::-1]:
        reversed += char
    print(reversed)





