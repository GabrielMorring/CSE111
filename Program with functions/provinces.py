


def main():
    
    text_list = []
    
    last_index = 0

    with open('provinces.txt') as data:
        
        for line in data:
            line = line.strip()
            text_list.append(line)
            last_index += 1
        
        last_index -= 2

    print(text_list)

    text_list.pop(0)
    text_list.pop(last_index)

    for i in range(len(text_list)):
        if text_list[i] == 'AB':
            text_list[i] = 'Alberta'
    
    alberta = 0

    for i in text_list:
        if i == 'Alberta':
            alberta += 1
    

    print(f'\nAlberta show\'s up {alberta} times.')

if __name__ == '__main__':
    main()