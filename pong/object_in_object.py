class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'"My name is {self.name}, bark bark!"')

class DogHouse:
    def __init__(self, price, dog):
        self.price = price
        self.dog = dog

    def describe(self):
        print('This dog house was bought for ${self.price}')
        print('Have you met the dog inside?')
        self.dog.bark()

my_dog = Dog('Latte')
my_dog_house = DogHouse(150, my_dog)
my_dog_house.describe()
