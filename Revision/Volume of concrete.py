def volume(l, w):
    v = 0
    d = 0

    while True:

        if types == 'residential':
            l = int(input(l))
            w = int(input(w))
            d = 0.5
            v = l * w * d
            break

        elif types == 'commercial':
            l = int(input(l))
            w = int(input(w))
            d = 0.25
            v = l * w * d
            break

        else:
            print('Enter building type type again!')
            continue

    return l, w, d, v

while True:
    types = input('Enter building type (residential / commercial): ')
    if types == 'X':
        break
    else:
        length, width, depth, vol = volume('Enter the length of the building: ',
                                           'Enter the width of the building: ')

    print(f'The volume of concrete required for a slab with a length of {length}m and width of {width}m '
          f'and a depth of {depth}m is {vol} cubic metres')