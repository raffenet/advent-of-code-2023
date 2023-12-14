#!/usr/bin/env python3

input = open('input.txt', 'r')
#input = open('sample.txt', 'r')

def convert_char(x):
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

def convert_str(a):
    ret = ''
    for c in a:
        ret += convert_char(c)
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

hands = [each.split() for each in input.readlines()]
for hand in hands:
    hand[0] = convert_str(hand[0])
hand_types = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
for hand in hands:
    hand_types[hand_type(hand)].append(hand)
out = []
for each in hand_types:
    hand_types[each].sort()
    out.extend(hand_types[each])

sum = 0
for i in range(len(out)):
    sum += (i + 1) * int(out[i][1])

print("part 1:", sum)

input.close()

exit(0)
