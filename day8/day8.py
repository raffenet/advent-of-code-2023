#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')
#input = open('sample2.txt', 'r')
#input = open('sample3.txt', 'r')

steps = input.readline().strip('\n')

nodes = {}
for each in input.readlines():
    if each != '\n':
        node = each.split('=')[0].strip()
        lr = each.split('=')[1].strip()
        nodes[node] = [lr.split(',')[0].strip('('),lr.split(', ')[1].strip(')')]

def step_to_index(x):
    if x == 'L':
        return 0
    elif x == 'R':
        return 1

def advance_step(x, loops):
    if x == len(steps) - 1:
        return 0, loops+1

    return x + 1, loops

cur = 'AAA'
step = 0
loops = 0
while cur != 'ZZZ':
    cur = nodes[cur][step_to_index(steps[step])]
    step, loops = advance_step(step, loops)

print("part 1:", step + (loops * len(steps)))

start = [each for each in nodes if each[-1] == 'A']
cycle = []
for each in start:
    step = 0
    loops = 0
    orig = each
    while each[-1] != 'Z':
        each = nodes[each][step_to_index(steps[step])]
        step, loops = advance_step(step, loops)
    cycle.append(step + loops * len(steps))

import math

print("part 2:", math.lcm(*cycle))

input.close()

exit(0)
