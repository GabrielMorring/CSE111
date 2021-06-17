from datetime import datetime 

current = datetime.now()

import math  

model = input('What is the model of your car? ')
width = int(input('\nWhat is the width of the tire in mm? '))
aspect_ratio = int(input('What is the aspect ration of the tire? '))
diameter = int(input('What is the diameter of the tire in inches? ')) 

volume = (math.pi * width**2 * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000
surf_area = math.pi * diameter * (width / 25.4)

print(f'\nThe approxmate volume of the tire is {volume:.1f} cubic cm. ')
print(f'The approxmate surface area of the outer edge ot the tire is {surf_area:.1f} square inches. ')

with open('deminsion.txt', 'at') as dimens_file:
    print(f'{current}, {model}, {width}, {aspect_ratio}, {diameter}, {volume}, {surf_area}', file = dimens_file)
