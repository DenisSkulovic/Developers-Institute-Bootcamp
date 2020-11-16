from typing import List


# Exercise 1: Cats
# Consider this class

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Instantiate 3 Cat objects using our class
# Create a function that finds the oldest cat and returns the cat
# Print out: “The oldest cat is , and is years old.” using the method previously created

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# brown_cat = Cat("Jack", 10)
# black_cat = Cat("John", 9)
# white_cat = Cat("Maxwell", 8)

# def oldest_cat(*cats):
#     oldest_cat = None
#     oldest_cat_age = 0
#     for cat in cats:
#         if cat.age > oldest_cat_age:
#             oldest_cat_age = cat.age
#             oldest_cat = cat
#     print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")







# Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : nameand height.
# This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the
# height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and
# his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print
# the name of the bigger dog.

# class Dog:

#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {2*self.height} cm high!")


# davids_dog = Dog("Rex", 50)

# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)

# sarahs_dog.bark()
# sarahs_dog.jump()

# if (davids_dog.height > sarahs_dog.height):
#     print(f"{davids_dog.name} is higher than {sarahs_dog.name}")
# elif (davids_dog.height == sarahs_dog.height):
#     print("Dogs are of same height")
# else:
#     print(f"{sarahs_dog.name} is higher than {davids_dog.name}")


# Exercise 3 : Who’s The Song Producer ?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


# class Song:

#     def __init__(self, lyrics: List):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()








# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds 
# the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. This method 
# removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them 
# together based on their first letter.
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example

# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:

    def __init__(self, zoo_name: str):
        self.name = zoo_name
        self.animals = []
        self.sorted_animals = {}


    def add_animal(self, new_animal: str):
        if new_animal in self.animals:
            print(f"{new_animal} is already in the zoo")

        else:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo")

    def get_animals(self):
        print("The zoo contains te following animals: \n", self.animals)

    def sell_animals(self, animal_sold):
        if animal_sold not in self.animals:
            print("This animal is not in the zoo")
        else:
            self.animals = self.animals.remove(animal_sold)
            print(f"{animal_sold} sold")

    def sort_animals(self):
        numbered_dict = {}
        letter_dict = {}
        for animal in self.animals:
            if animal[0] not in letter_dict:
                letter_dict[animal[0]] = [animal]
            else:
                letter_dict[animal[0]] += [animal]
        for pair in zip(range(1, len(sorted(letter_dict.keys()))+1), sorted(letter_dict.keys())):
            numbered_dict[pair[0]] = letter_dict[pair[1]]
        self.sorted_animals = numbered_dict

    def get_groups(self):
        if self.sorted_animals.__len__() == 0:
            print("Animals are not grouped yet.")
            return None
        print("\nAnimal groups are: ")
        for _, group in self.sorted_animals.items():
            print(group)
            


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Dog")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Wolf")
ramat_gan_safari.add_animal("Liger")
ramat_gan_safari.add_animal("Duck")

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()



