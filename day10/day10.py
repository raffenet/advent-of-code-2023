#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')
#input = open('sample2.txt', 'r')
grid = input.readlines()

def next(direction, tile):
    if tile == 'S':
        return 'done'
    elif direction == 'north':
        if tile == '|':
            return 'north'
        elif tile == '7':
            return 'west'
        elif tile == 'F':
            return 'east'
    elif direction == 'south':
        if tile == '|':
            return 'south'
        elif tile == 'L':
            return 'east'
        elif tile == 'J':
            return 'west'
    elif direction == 'west':
        if tile == '-':
            return 'west'
        elif tile == 'F':
            return 'south'
        elif tile == 'L':
            return 'north'
    elif direction == 'east':
        if tile == '-':
            return 'east'
        elif tile == 'J':
            return 'north'
        elif tile == '7':
            return 'south'

    return 'deadend'

def move(direction, x, y):
    if direction == 'north':
        return x, y-1
    elif direction == 'south':
        return x, y+1
    elif direction == 'west':
        return x-1, y
    elif direction == 'east':
        return x+1, y

start = (0, 0)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            start = (x,y)

dirs = ['north', 'south', 'east', 'west']
direction = dirs.pop()
while True:
    x = start[0]
    y = start[1]
    x, y = move(direction, x, y)
    length = 1
    tile = grid[y][x]
    direction = next(direction, tile)
    if direction == 'deadend':
        direction = dirs.pop()
        continue
    while direction != 'done' and direction != 'deadend':
        x, y = move(direction, x, y)
        length += 1
        tile = grid[y][x]
        direction = next(direction, tile)
        if direction == 'deadend':
            direction = dirs.pop()
            break
    if direction == 'done':
        break

print("part 1:", length/2)

input.close()
exit(0)
