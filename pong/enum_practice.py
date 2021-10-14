from enum import Enum

class TrafficLight(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


# light_color = TrafficLight.GREEN

# if light_color == TrafficLight.GREEN:
#     print('Let\'s go!!!')
# elif light_color == TrafficLight.YELLOW:
#     print('Hey, slow down')
# elif light_color == TrafficLight.RED:
#     print('Stop stop stop!')
# else:
#     print('What color is that?')

light_color = 'green'

if light_color == 'greeen':
    print('Let\'s go!!!')
elif light_color == 'yellw':
    print('Hey, slow down')
elif light_color == 'red':
    print('Stop stop stop!')
else:
    print('What color is that?')