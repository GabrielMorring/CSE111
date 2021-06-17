import math

manu_items = int(input('What is the number of manufactured items? '))
user_items = int(input('What is the number of items the user pack will pack per box? '))
boxes = manu_items / user_items
boxes = math.ceil(boxes)
print(f'For {manu_items} items, packing {user_items} items in each box, you will need {boxes} boxes.')