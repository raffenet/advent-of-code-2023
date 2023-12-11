#!/usr/bin/env python3

sample = [(7,9),(15,40),(30,200)]
input = [(60,601),(80,1163),(86,1559),(76,1300)]
part2 = (60808676,601116315591300)

error = 1
for each in input:
    wins = 0
    for i in range(1,each[0]):
        dist = i * (each[0] - i)
        if (dist > each[1]):
            wins += 1
    error *= wins

print("part 1:", error)

wins = 0
for i in range(1,part2[0]):
    dist = i * (part2[0] - i)
    if (dist > part2[1]):
        wins += 1

print("part 2:", wins)

exit(0)
