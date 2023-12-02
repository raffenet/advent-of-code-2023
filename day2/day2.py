#!/usr/bin/env python3

input = open('input.txt', 'r')

ref = {
    'red': 12,
    'green': 13,
    'blue':14,
}

sum = 0
for game in input.readlines():
    id = int(game.split(':')[0].split(' ')[1])
    impossible = False

    for round in game.split(': ')[1].split('; '):
        for cubes in [each.split(' ') for each in round.split(', ')]:
            num = int(cubes[0])
            color = cubes[1].strip()
            if num > ref[color]:
                impossible = True
                break
        if impossible:
            break

    if not impossible:
        sum += id

print('part 1: ' + str(sum))

input.seek(0)

powersum = 0
for game in input.readlines():
    maxes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for round in game.split(': ')[1].split('; '):
        for cubes in [each.split(' ') for each in round.split(', ')]:
            num = int(cubes[0])
            color = cubes[1].strip()
            if num > maxes[color]:
                maxes[color] = num

    powersum += maxes['red'] * maxes['green'] * maxes['blue']

print('part 2: ' + str(powersum))

input.close()

exit(0)
