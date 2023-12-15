#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

hists = [list(map(lambda x: int(x), each.split())) for each in input.readlines()]

part1 = 0
part2 = 0
for each in hists:
    forward_diffs = [each[-1]]
    reverse_diffs = [each[0]]

    while True:
        tmp = []
        for i in range(len(each) - 1):
            tmp.append(each[i + 1] - each[i])
        if tmp.count(0) == len(tmp):
            break
        forward_diffs.append(tmp[-1])
        reverse_diffs.insert(0, tmp[0])
        each = tmp

    part1 += sum(forward_diffs)

    back = 0
    for each in reverse_diffs:
        back = each - back
    part2 += back

print("part 1:", part1)
print("part 2:", part2)

input.close()

exit(0)
