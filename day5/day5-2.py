#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

seeds = [int(each) for each in input.readline().split(':')[1].split()]
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))

maps = []
for line in input.readlines():
    if 'map:' in line:
        maps.append([])
        continue
    if line == '\n':
        continue

    dst = int(line.split()[0])
    src = int(line.split()[1])
    length = int(line.split()[2])
    delta = src - dst
    maps[-1].append((range(dst, dst + length), delta))
maps.reverse()

loc2 = -1
potential = 0
while loc2 == -1:
    orig = potential
    for m in maps:
        for r in m:
            if potential in r[0]:
                potential += r[1];
                break;
    for seed_range in seed_ranges:
        if potential in seed_range:
            loc2 = orig
            break
    potential = orig + 1

print("part 2:", loc2)
input.close()

exit(0)
