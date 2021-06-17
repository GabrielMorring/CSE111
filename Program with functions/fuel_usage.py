def calc_mpg(end, start, gallons):
    return (end - start) / gallons

def calc_lp100k_from_mpg(mpg):
    return 235.215 / mpg

def main():
    start = float(input('What is your starting odometer valuein miles? '))
    end = float(input('What is your ending odometer value in miles? '))
    fuel = float(input('What is your amount of fuel in gallons? '))

    mpg = calc_mpg(end, start, fuel)
    lp100k = calc_lp100k_from_mpg(mpg)

    print(f'Your fuel efficiency in miles per gallon is {mpg:.1f}.')
    print(f'Your fuel efficiency in liters per 100 kilometers is  is {lp100k:.1f}.')

main()

