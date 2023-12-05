#!/usr/bin/env python3

from collections import Counter

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

score = 0
cards = Counter()
for game in input.readlines():
    # part 1
    winners = set([int(each) for each in game.split('|')[0].split(":")[1].split()])
    numbers = set([int(each) for each in game.split('|')[1].split()])
    matches = len(winners.intersection(numbers))
    if (matches > 0):
        score += 2**(matches - 1)

    # part 2
    game_id = int(game.split(':')[0].split()[1])
    cards[game_id] += 1
    for each in range(game_id+1, game_id+1+matches):
        cards[each] += cards[game_id]

print('part 1:', score)
print('part 2:', sum(cards.values()))

input.close()

exit(0)
