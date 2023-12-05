#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

score = 0
cards = []
for game in input.readlines():
    # part 1
    winners = set([int(each) for each in game.split('|')[0].split(":")[1].split()])
    numbers = set([int(each) for each in game.split('|')[1].split()])
    matches = len(winners.intersection(numbers))
    if (matches > 0):
        score += 2**(matches - 1)

    # part 2
    game_id = int(game.split(':')[0].split()[1])
    cards.append(game_id)
    cards.extend([each for each in range(game_id+1, game_id+1+matches)]*cards.count(game_id))

print('part 1: ' + str(score))
print('part 2: ' + str(len(cards)))

input.close()

exit(0)
