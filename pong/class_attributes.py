class Cat:
    num_tails = 1

    def __init__(self, name, lives=9):
        self.name = name
        self.lives = lives

    def meow(self):
        print(f'Meow, my name is {self.name}')
        print(f'I have {self.lives} lives')

    @classmethod
    def wag_tail(cls):
        print(cls)
        print('I am a cat, I wag my tail')

    @staticmethod
    def wag_tail_static():
        print('I am a cat, I wag my tail')


cat_1 = Cat('Mimi')
cat_1.meow()

cat_2 = Cat('Simba', 8_000)
cat_2.meow()

# Cat.wag_tail()

cat_1.wag_tail()
cat_2.wag_tail()








# class Dog:
#     num_legs = 4
#     num_tails = 1
#     def __init__(self, name, age):
#         self.name = name.title()
#         self.age = age

# dog_1 = Dog(name='didi', age=10)
# print(dog_1.name)
# dog_2 = Dog('fifi', age=5)

# print(Dog.num_legs)
# print(Dog.num_tails)

# print(dog_1.num_legs)

# dog_1.num_legs = 5
# print('dog_1 has', dog_1.num_legs, 'legs')
# print(f'dog_1 has {dog_1.num_legs} legs')
# print('dog_1 has ' + str(dog_1.num_legs) + ' legs')
# print('Dog the class has', Dog.num_legs, 'legs')