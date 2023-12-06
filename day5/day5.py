#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

seeds = [int(each) for each in input.readline().split(':')[1].split()]

maps = []
for line in input.readlines():
    if 'map:' in line:
        maps.append({})
        continue
    if line == '\n':
        continue

    dst = int(line.split()[0])
    src = int(line.split()[1])
    length = int(line.split()[2])
    maps[-1][range(src,src+length)] = dst - src

locations = []
for seed in seeds:
    for m in maps:
        for r in m:
            if r.__contains__(seed):
                seed += m[r]
                break
    locations.append(seed)

print('part 1:', min(locations))
input.close()

exit(0)
