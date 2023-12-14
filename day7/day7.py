#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

def convert_char(x, joker=False):
    if joker:
        if x == 'J':
            return 'a'
        if x == '2':
            return 'b'
        elif x == '3':
            return 'c'
        elif x == '4':
            return 'd'
        elif x == '5':
            return 'e'
        elif x == '6':
            return 'f'
        elif x == '7':
            return 'g'
        elif x == '8':
            return 'h'
        elif x == '9':
            return 'i'
        elif x == 'T':
            return 'j'
        elif x == 'Q':
            return 'k'
        elif x == 'K':
            return 'l'
        elif x == 'A':
            return 'm'
    else:
        if x == '2':
            return 'a'
        elif x == '3':
            return 'b'
        elif x == '4':
            return 'c'
        elif x == '5':
            return 'd'
        elif x == '6':
            return 'e'
        elif x == '7':
            return 'f'
        elif x == '8':
            return 'g'
        elif x == '9':
            return 'h'
        elif x == 'T':
            return 'i'
        elif x == 'J':
            return 'j'
        elif x == 'Q':
            return 'k'
        elif x == 'K':
            return 'l'
        elif x == 'A':
            return 'm'

def convert_str(a, joker=False):
    ret = ''
    for c in a:
        ret += convert_char(c, joker)
    return ret

def hand_type(hand):
    if len(set(hand[0])) == 1:
        # five of a kind
        return 6
    elif len(set(hand[0])) == 2:
        # 4 of a kind or full house
        if max([hand[0].count(each) for each in set(hand[0])]) == 4:
            return 5
        else:
            return 4
    elif len(set(hand[0])) == 3:
        # three of a kind or two pair
        if max([hand[0].count(each) for each in set(hand[0])]) == 3:
            return 3
        else:
            return 2
    elif len(set(hand[0])) == 4:
        # one pair
        return 1

    # high card
    return 0

def joker_hand_type(hand):
    # must be careful to count empty set for 'JJJJJ' using <= 1
    if len(set(hand[0]).difference('J')) <= 1:
        # five of a kind
        return 6
    elif len(set(hand[0]).difference('J')) == 2:
        # 4 of a kind or full house
        num_j = hand[0].count('J')
        if max([hand[0].count(each) for each in set(hand[0]).difference('J')]) + num_j == 4:
            return 5
        else:
            return 4
    elif len(set(hand[0]).difference('J')) == 3:
        # three of a kind or two pair
        num_j = hand[0].count('J')
        if max([hand[0].count(each) for each in set(hand[0]).difference('J')]) + num_j == 3:
            return 3
        else:
            return 2
    elif len(set(hand[0]).difference('J')) == 4:
        # one pair
        return 1

    # high card
    return 0

hands = [each.split() for each in input.readlines()]
hand_types = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
for hand in hands:
    converted_hand = [convert_str(hand[0]), hand[1]]
    hand_types[hand_type(hand)].append(converted_hand)
out = []
for each in hand_types:
    hand_types[each].sort()
    out.extend(hand_types[each])
sum = 0
for i in range(len(out)):
    sum += (i + 1) * int(out[i][1])

joker_hand_types = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
for hand in hands:
    converted_hand = [convert_str(hand[0],True), hand[1]]
    joker_hand_types[joker_hand_type(hand)].append(converted_hand)
joker_out = []
for each in joker_hand_types:
    joker_hand_types[each].sort()
    joker_out.extend(joker_hand_types[each])
joker_sum = 0
for i in range(len(joker_out)):
    joker_sum += (i + 1) * int(joker_out[i][1])

print("part 1:", sum)
print("part 2:", joker_sum)

input.close()

exit(0)
