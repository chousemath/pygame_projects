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

current_light = TrafficLight.GREEN

if current_light == TrafficLight.GREEN:
    print('Go go go!')
elif current_light == TrafficLight.YELLOW:
    print('Woah, slow down.')
elif current_light == TrafficLight.RED:
    print('Stop!!!')
else:
    print('Unidentified light color')
