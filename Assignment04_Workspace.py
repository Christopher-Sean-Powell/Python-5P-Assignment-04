__author__ = 'Chris'

import random

def cards_at_rank (rank):
    '''This will print a list of 4 values, consisting of the specified rank of all 4 suits. The values in the list are
    strings.'''
    partial_deck = []
    for suit in'CDHS':
        card = rank + suit
        partial_deck.append(card)
    return partial_deck

def full_deck():
    '''This will construct the whole deck, as a list, using the function cards_at_rank to make the 4 cards of each suit
    per rank.'''
    deck = []
    for r in '23456789TJQKA':
        this_rank = cards_at_rank(r)
        deck += this_rank
    return deck


def suit_list (hand):
    '''This function takes a hand of cards and constructs a new list only consisting of the suits'''
    suit_list = []
    for i in range (5):
        suit_list += hand[i][1]
    return suit_list

def count_suit (hand):
    '''This function uses suite_list to turn the list of suits into a new list that counts the number of each suit'''
    suit_count = [0, 0, 0, 0]
    suite_list = suit_list(hand)
    for n in range (5):
        if suite_list[n] == 'C':
            suit_count[0] += 1
        if suite_list[n] == 'D':
            suit_count[1] += 1
        if suite_list[n] == 'H':
            suit_count[2] += 1
        if suite_list[n] == 'S':
            suit_count[3] += 1
    return suit_count

def rank_list (hand):
    '''This function takes a hand of cards and constructs a new list consisting of only the rank of each card'''
    rank_list = []
    for i in range (5):
        rank_list += hand[i][0]
    return rank_list

def count_rank (hand):
    '''This function uses rank_list to turn the list of ranks into a new list that counts the number of each rank'''
    rank_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ranking_list = rank_list(hand)
    for r in range (5):
        if ranking_list[r] == '2':
            rank_count[0] += 1
        elif ranking_list[r] == '3':
            rank_count[1] += 1
        elif ranking_list[r] == '4':
            rank_count[2] += 1
        elif ranking_list[r] == '5':
            rank_count[3] += 1
        elif ranking_list[r] == '6':
            rank_count[4] += 1
        elif ranking_list[r] == '7':
            rank_count[5] += 1
        elif ranking_list[r] == '8':
            rank_count[6] += 1
        elif ranking_list[r] == '9':
            rank_count[7] += 1
        elif ranking_list[r] == 'T':
            rank_count[8] += 1
        elif ranking_list[r] == 'J':
            rank_count[9] += 1
        elif ranking_list[r] == 'Q':
            rank_count[10] += 1
        elif ranking_list[r] == 'K':
            rank_count[11] += 1
        elif ranking_list[r] == 'A':
            rank_count[12] += 1
    return rank_count

def string_ranks (hand):
    '''This function takes the output of count_rank (a list) and turns it into a string'''
    counts = ''
    for num in count_rank(hand):
        counts += str (num)
    return counts

def string_suits (hand):
    '''This function takes the output of count_suit (a list) and turns it into a string'''
    counts = ''
    for num in count_suit(hand):
        counts += str(num)
    return counts

def get_rank (card):
    '''This function takes the input of one card and returns the rank of that card on a scale from 0 to 12.'''
    rank_card = 0
    if card[0] == '2':
        rank_card += 0
    elif card[0] == '3':
        rank_card += 1
    elif card[0] == '4':
        rank_card += 2
    elif card[0] == '5':
        rank_card += 3
    elif card[0] == '6':
        rank_card += 4
    elif card[0] == '7':
        rank_card += 5
    elif card[0] == '8':
        rank_card += 6
    elif card[0] == '9':
        rank_card += 7
    elif card[0] == 'T':
        rank_card += 8
    elif card[0] == 'J':
        rank_card += 9
    elif card[0] == 'Q':
        rank_card += 10
    elif card[0] == 'K':
        rank_card += 11
    elif card[0] == 'A':
        rank_card += 12
    return rank_card

def get_suit (card):
    card_suit = 0
    if card[1] == 'C':
        card_suit += 0
    elif card[1] == 'D':
        card_suit += 1
    elif card[1] == 'H':
        card_suit += 2
    elif card[1] == 'S':
        card_suit += 3
    return card_suit

# ^^ All of the functions above this point are the "basic" functions that are used in the other, more complex functions
# below. Note that the function get_suit is never actually utilized, but kept it for the future (just in case).


def find_4_of_kind (hand):
    string_of_ranks = string_ranks(hand)
    four_of_kind = 0
    for y in range (0, 13):
        if string_of_ranks[y] == '4':
            four_of_kind += 1
        else:
            four_of_kind += 0
    return four_of_kind


def find_flush (hand):
    '''This function takes the return of the string_suits function and checks if any of the values are 5, indicating
    a flush'''
    string_of_suits = string_suits(hand)
    flush = 0
    for x in range(0, 4):
        if (string_of_suits)[x] == '5':
            flush += 1
    return flush


def find_straight (hand):
    '''This function takes the return of the string_ranks function and checks if there is the proper pattern
    corresponding to a straight. Returns a '1' or a '0'.'''
    string_of_ranks = string_ranks(hand)
    straight = 0
    for i in range(0, 13):
        if string_of_ranks[i] > 1:
            straight += 0
    if string_of_ranks == '1111100000000':
        straight += 1
    elif string_of_ranks == '0111110000000':
        straight += 1
    elif string_of_ranks == '0011111000000':
        straight += 1
    elif string_of_ranks == '0001111100000':
        straight += 1
    elif string_of_ranks == '0000111110000':
        straight += 1
    elif string_of_ranks == '0000011111000':
        straight += 1
    elif string_of_ranks == '0000001111100':
        straight += 1
    elif string_of_ranks == '0000000111110':
        straight += 1
    elif string_of_ranks == '0000000011111':
        straight += 1
    else:
        straight += 0
    return straight


def find_3_of_kind (hand):
    '''This function takes the return of the string_ranks function and checks to see if any of the indices are '3',
    indicating 3-of-a-kind. Returns a '1' or a '0'.'''
    string_of_ranks = string_ranks(hand)
    three_of_kind = 0
    for k in range (0, 13):
        if string_of_ranks[k] == '3':
            three_of_kind += 1
        else:
            three_of_kind += 0
    return three_of_kind


def find_num_pairs (hand):
    '''This function takes the return of the string_ranks function and checks to see how many of the indices are '2',
    indicating a pair, and then returns the number of those instances (0, 1, or 2).'''
    string_of_ranks = string_ranks(hand)
    num_pair = 0
    for l in range (0, 13):
        if string_of_ranks[l] == '2':
            num_pair += 1
        else:
            num_pair += 0
    return num_pair


def high_card (hand):
    all_ranks = []
    new_card = 0
    for i in range (5):
        card = hand[i]
        get_ranks = get_rank(card)
        all_ranks += [get_ranks]
    all_ranks.sort()
    high_card = all_ranks[-1]
    for b in range (0,5):
        if high_card == get_rank(hand[b]):
            new_card = (hand[b])
        else:
            pass
    high_card_value = deck.index(new_card)
    return high_card_value


def rankpokerhand (hand):
    '''This function takes the output of all the other functions that check the status of a given hand and compares them,
    returning the overall rank of that hand. Returns a number between 1 and 8, or if the hand is High Card it
    returns the index of that card in the original deck.'''
    rank = 0
    if find_flush(hand) == 1 and find_straight(hand) == 1:
        rank += 1
    elif find_4_of_kind (hand) == 1:
        rank += 2
    elif find_3_of_kind(hand) == 1 and find_num_pairs(hand) == 1:
        rank += 3
    elif find_flush(hand) == 1:
        rank += 4
    elif find_straight(hand) == 1:
        rank += 5
    elif find_3_of_kind(hand) == 1:
        rank += 6
    elif find_num_pairs(hand) == 2:
        rank += 7
    elif find_num_pairs(hand) == 1:
        rank += 8
    else:
        rank += high_card(hand)
    return rank


def hand_string (hand_rank):
    '''This function takes an integer input denoting the rank of a poker hand and returns the string name of the type of hand that the integer corresponds to. For any number 10 or greater, it returns the card associated with that index number in the deck.'''
    hands_list = ["Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pair", "Pair",
                  "High Card"]
    hand_name = ''
    if hand_rank == 1:
        hand_name = hands_list[0]
    elif hand_rank == 2:
        hand_name = hands_list[1]
    elif hand_rank == 3:
        hand_name = hands_list[2]
    elif hand_rank == 4:
        hand_name = hands_list[3]
    elif hand_rank == 5:
        hand_name = hands_list[4]
    elif hand_rank == 6:
        hand_name = hands_list[5]
    elif hand_rank == 7:
        hand_name = hands_list[6]
    elif hand_rank == 8:
        hand_name = hands_list[7]
    elif hand_rank == 9:
        hand_name = hands_list[8]
    elif hand_rank >= 10:
        hand_name = deck[hand_rank]
    return hand_name


def monte_carlo (number_of_hands):
    percent_each_hand =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hand_rank_count = []
    num_each_hand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in range (number_of_hands):
        hand = random.sample(deck, 5)
        rank_poker_hand = rankpokerhand(hand)
        hand_rank_count += [rank_poker_hand]
    hand_rank_count.sort()
    for h in range (number_of_hands):
        if hand_rank_count[h] == 1:
            num_each_hand[1] += 1
        elif hand_rank_count[h] == 2:
            num_each_hand[2] += 1
        elif hand_rank_count[h] == 3:
            num_each_hand[3] += 1
        elif hand_rank_count[h] == 4:
            num_each_hand[4] += 1
        elif hand_rank_count[h] == 5:
            num_each_hand[5] += 1
        elif hand_rank_count[h] == 6:
            num_each_hand[6] += 1
        elif hand_rank_count[h] == 7:
            num_each_hand[7] += 1
        elif hand_rank_count[h] == 8:
            num_each_hand[8] += 1
        elif hand_rank_count[h] >= 9:
            num_each_hand[9] += 1
    lists_each_hand = num_each_hand
    for m in range (0,10):
        percent_each_hand[m] += (lists_each_hand[m] / float(number_of_hands)) * 100
    return percent_each_hand


# This piece makes it so that if the program is run standalone it will perform the definitions and loop below; if the
# program is loaded as a module it will instead solely define deck as shown.

if __name__ == '__main__':
    deck = full_deck()
    percentages = monte_carlo (10000)
    for k in range (1,10):
        print '{0:18s} : {1:.2f}%'.format(hand_string(k), percentages[k])


else:
    deck = full_deck()