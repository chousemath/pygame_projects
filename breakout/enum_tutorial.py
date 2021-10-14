from enum import Enum

# Enum is a useful class for creating
# child classes. You generally use an
# enum (enumeration) when you have a
# small range of values that you want
# to represent using more meaningful
# names. You also get the added benefit
# that Python will check to make sure
# that the enum value you specify is
# "valid" (pre-defined), saving you from
# potential typing mistakes


class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 3


# Use one of the "class attributes"
# of the TrafficLight class to represent
# the color of the curent signal
current_light = TrafficLight.GREEN

# You again use the "class attributes" of
# the TrafficLight class to check the value
# of current_light
if current_light == TrafficLight.GREEN:
    print("Go go go!")
elif current_light == TrafficLight.YELLOW:
    print("Woah, slow down.")
elif current_light == TrafficLight.RED:
    print("Stop!!!")
else:
    print("Unidentified light color")

# Class attributes are different from instance
# attributes. Class attributes are owned by
# the class itself. Instance attributes are
# owned by individual instances of that class.
# The same goes for methods. You can have class
# methods and instance methods.

class Dog:
    num_legs = 4 # class attribute

    def __init__(self, name, age):
        '''Constructor function'''
        self.name = name # instance attribute
        self.age = age # instance attribute

fido = Dog('Fido', 8)
# You access instance attributes on the
# object instance
print(f'{fido.name} is of age {fido.age}')
# You access class attributes through the
# class itself
print(f'All dogs have {Dog.num_legs} legs')
# Instances also have access to class
# attributes (which can be a little confusing)
print(f'{fido.name} has {fido.num_legs} legs')

try:
    # this will fail
    print(f'All dogs have the name "{Dog.name}"')
except Exception as e:
    print('Error:', e)

try:
    # this will also fail
    print(f'All dogs have the age "{Dog.age}"')
except Exception as e:
    print('Error:', e)

# Instances have access to class attributes,
# that makes sense

# Classes do not have access to the instance
# attributes of their individual, unique
# instances, that also makes sense

# Class methods require a "decorator" to mark
# them as class methods
class Cat:
    num_tails = 1

    def __init__(self, name, lives):
        '''Constructor function'''
        self.name = name
        self.lives = lives

    def meow(self):
        '''An instance method'''
        print(f'Meow, my name is {self.name}')
        print(f'I have {self.lives} lives')

    @classmethod
    def wag_tail(cls):
        '''
        A class method, the implicit first argument is the class
        '''
        print(f'The cat wagged its {Cat.num_tails} tail(s)')
        print(f'Printed from the class {cls}')

    @staticmethod
    def wag_tail_static():
        '''
        A class method, the implicit first argument is the class
        '''
        print(f'The cat wagged its {Cat.num_tails} tail(s)')


fluff = Cat('Fluff', 9)
fluff.meow()

Cat.wag_tail()
fluff.wag_tail()

Cat.wag_tail_static()
fluff.wag_tail_static()

