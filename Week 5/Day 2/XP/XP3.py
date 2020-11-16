from XP import Dog
import random

# Exercise 2 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”


class PetDog(Dog):

    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        super().bark()
        self.trained = True

    def play(self, *dogs):
        dog_names = [dog.name for dog in dogs]
        print(", ".join(dog_names) + " play together.")
        for dog in dogs:
            self.trained = False
            dog.trained = False
    
    def do_a_trick(self):
        if self.trained == True:
            sentences = [f"{self.name} does a barrel roll", f"{self.name} stands on their back legs", f"{self.name} shakes your hand", f"{self.name} plays dead"]
            random.shuffle(sentences)
            print(sentences[0])