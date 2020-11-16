# Daily Challenge : Old MacDonald’s Farm
# Look carefully at this code and output
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!

# Create the code that is needed to recreate the code above. Here are a few questions to help give you some direction:
# 1. Create a Farm class. How do we implement that?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many method does the Farm class need ?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should
# this function have? How many…?
# 5. Test that your code works and gives the same results as the example above.
# 6. Bonus: line up the text nicely in columns like in the example using string formatting

# Expand The Farm
# Add a method to the Farm class called get_animal_types. It should return a sorted list of all the animal types
# (names) that the farm has in it. For the example above, the list should be: ['cow', 'goat', 'sheep']
# Add another method to the Farm class called get_short_info. It should return a string like this: “McDonald’s farm
# has cows, goats and sheep.”
# It should call the get_animal_types function.
# How would we make sure each of the animal names printed has a comma after it aside from the one before last
# (has an and after) and the last(has a period after)?.


class Farm:

    def __init__(self, farmer_surname):
        self.farmer_surname = farmer_surname
        self.animals = {}

    def add_animal(self, new_animal, quantity=1):
        if new_animal not in self.animals.keys():
            self.animals[new_animal] = quantity
        else:
            self.animals[new_animal] += quantity
        print(self.animals)

    def get_info(self):
        for key, value in self.animals.items():
            print(key, ": ", value)
        print("\nI-E-A-I-A-I-O!")

    def get_animal_types(self):
        return list(self.animals.keys())

    def get_short_info(self):
        strng = f"{self.farmer_surname}'s farm has "
        types = self.get_animal_types()
        for animal in types:
            if len(types) == 1:
                strng += f"{animal}s."
                print(strng)
                return None
            elif types.index(animal) == len(types)-1:
                strng += f"and {animal}s."
            elif types.index(animal) == len(types)-2:
                strng += f"{animal}s "            
            else:
                strng += f"{animal}s, "
        print(strng)


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_short_info()
