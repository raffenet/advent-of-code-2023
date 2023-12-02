#!/usr/bin/env python3

ref = {
    'red': 12,
    'green': 13,
    'blue':14,
}

sum = 0

input = open('input.txt', 'r')
for game in input.readlines():
    id = int(game.split(':')[0].split(' ')[1])
    impossible = False

    for round in game.split(': ')[1].split('; '):
        for cubes in [each.split(' ') for each in round.split(', ')]:
            if int(cubes[0]) > ref[cubes[1].strip()]:
                impossible = True
                break
        if impossible:
            break

    if not impossible:
        sum += id

print(sum)

exit(0)
