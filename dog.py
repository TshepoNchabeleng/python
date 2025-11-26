class Dog:
    # A simple attempt to model a dog

    def __init__ (self, name, age): # initialize name and dog attributes
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("Willie", 6)

my_dog.sit()
my_dog.roll_over()