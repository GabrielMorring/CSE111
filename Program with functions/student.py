import csv


def main():

    dentists = read_dict('students.csv')

    i_number = input('Enter an I number: ')


    if i_number in dentists:

        name = dentists[i_number]


        print(name)
    else:
        print('No such student.')
            

def read_dict(filename):
    
    dictionary = {}

    with open(filename, 'rt') as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:

            key = row[0]

            dictionary[key] = row[1]

    return dictionary


if __name__ == '__main__':
    main()

