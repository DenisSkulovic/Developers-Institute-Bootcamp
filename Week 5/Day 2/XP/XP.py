# Exercise 1 : Pets
# Consider this code
# Add another cat breed
# Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# Instantiate the Pet class with all your cats. Use the variable my_pets
# Output all of the cats walking using the my_pets instance

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class BrownCat(Cat):

#     def __init__(self, name, age, brown_tone):
#         super().__init__(name, age)
#         self.brown_tone = brown_tone

# my_bengal = Bengal("Jack", 10)
# my_chartreux = Chartreux("Jim", 8)
# my_browncat = BrownCat("Montgomery", 3, "very brown")

# my_cats = [my_bengal, my_chartreux, my_browncat]

# my_pets = Pets(my_cats)
# my_pets.walk()








# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
# Create 3 dogs and use some of your methods

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} barks!")

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        dog_score = self.weight * self.run_speed()
        other_dog_score = other_dog.weight * other_dog.run_speed()
        winner = None
        if dog_score > other_dog_score:
            winner = self.name
        elif other_dog_score > dog_score:
            winner = other_dog.name
        else:
            return "It's a draw."
        return f"{winner} won the fight!"

# jimmy = Dog("Jimmy", 10, 100)
# johnny = Dog("Johnny", 9, 90)
# jackie = Dog("Jackie", 8, 110)

# print(jimmy.fight(johnny))



