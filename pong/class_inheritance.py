# Inheritance enables us to define
# a child class (derived class) that
# takes all the functionality from a
# parent class (base class) and allows
# us to add more.

# Inheritance refers to defining a new
# class with little or no modification
# to an existing class. This results in
# more reusable code.

# The new class is called derived
# (or child) class and the one from
# which it inherits is called the
# base (or parent) class.

# Here is the general syntax for class
# inheritance

class BaseClass: # also called "Parent"
    pass

class DerivedClass(BaseClass): # also called "Child"
    pass

# Here is a more concrete example of
# inheritance in action

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perim(self):
        return 2 * self.width + 2 * self.height

class Square(Rectangle):
    '''
    Square is a subset of rectangle,
    so all squares are rectangles
    '''
    def __init__(self, side):
        # super() is a reference to the parent class
        super().__init__(side, side)
        self.side = side

        # If no __init__() method is implemented
        # in the inherited class, then the parent
        # __init__() will be called automatically
        # when an object of the inherited class is
        # created.

        # If __init__() is implemented in the
        # inherited class, then that will override
        # the parent class method.

        # The parent class method will NOT be called
        # unless the call is written in the inherited
        # class.

    def say_hello(self):
        print(f'Hi I am a {self.side} x {self.side} square')
        print(f'  * {self.width}W x {self.height}H')

rect_1 = Rectangle(10, 20)
assert rect_1.get_area() == 200
assert rect_1.get_perim() == 60

rect_2 = Rectangle(5, 15)
assert rect_2.get_area() == 75
assert rect_2.get_perim() == 40

sq_1 = Square(25)
assert sq_1.get_area() == 625
assert sq_1.get_perim() == 100
sq_1.say_hello()

sq_2 = Square(100)
assert sq_2.get_area() == 10_000
assert sq_2.get_perim() == 400
sq_2.say_hello()
