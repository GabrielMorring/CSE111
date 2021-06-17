from datetime import datetime

current = datetime.now()

weekday = current.isoweekday()

# weekday = 1



def calc_discount(subtotal):
    return subtotal / 10

def calc_sales_tax(subtotal):
    return subtotal * .06


def calc_total(subtotal, tax, discount):
    return subtotal - discount + tax

subtotal = float(input('Enter your subtotal. '))

tax = calc_sales_tax(subtotal)

if weekday == 2 or weekday == 3:
    if subtotal >= 50:
        discount = calc_discount(subtotal)
    else:
        discount = 0
        difference = 50 - subtotal
else: 
      discount = 0

total = calc_total(subtotal, tax, discount)

print(f'Discount amount: ${discount:.2f} ')
print(f'Sales Tax amount ${tax:.2f}')
if weekday == 2 or weekday == 3:
    if subtotal < 50:
        print(f'If you spend ${difference:.2f} more you will get a 10% discount.')
print(f'Total: ${total:.2f}')

