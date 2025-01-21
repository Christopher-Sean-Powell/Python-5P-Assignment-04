__author__ = 'Chris'

# def rankpokerhand(hand):


# Build the function by parts-

# sample input: ["AS", "5D", "TD", "5C", "JH"]

# This part determines if the hand is a flush.

def find_flush (hand):
 if (hand[0])[1] == (hand[1])[1] == (hand[2])[1] == (hand[3])[1] == (hand[4])[1]:
     return 4
 else:
     return 0  # Not really sure what to make this return, maybe switch to Boolean statements...make it return flush = false, and make the part above return flush = true. Otherwise, not sure.


# This function checks for pairs, 3 of kind and 4 of kind. It returns the "number of a kind" after (2, 3, or 4). Not really useful for full house, but I suppose I can make an if statement within the total rankpokerhand function for if the result of this is 0 it returns the high card, and if the result is 2 or 3 it checks to see if it is a full house...That may work.

def number_of_a_kind (hand):
    pair = []
    if (hand[0])[0] == (hand[1])[0]:
        pair += [str((hand[0])[0]) + str((hand[1])[0])]

    elif (hand[0])[0] == (hand[2])[0]:
        pair += [str((hand[0])[0] + (hand[2])[0])]

    elif (hand[0])[0] == (hand[3])[0]:
        pair += [str((hand[0])[0] + (hand[3])[0])]

    elif (hand[0])[0] == (hand[4])[0]:
        pair += [str((hand[0])[0] + (hand[4])[0])]

    if (hand[1])[0] == (hand[2])[0]:
        pair += [str((hand[1])[0] + (hand[2])[0])]

    elif (hand[1])[0] == (hand[3])[0]:
        pair += [str((hand[1])[0] + (hand[3])[0])]

    elif (hand[1])[0] == (hand[4])[0]:
        pair += [str((hand[1])[0] + (hand[4])[0])]

    if (hand[2])[0] == (hand[3])[0]:
        pair += [str((hand[2])[0] + (hand[3])[0])]

    elif (hand[2])[0] == (hand[4])[0]:
        pair += [str((hand[2])[0] + (hand[4])[0])]

    if (hand[3])[0] == (hand[4])[0]:
        pair += [str((hand[3])[0] + (hand[4])[0])]

    if pair == []:
        return 0   # May want to make this return a different value, like an empty string or list.

    return pair   # Note: the output appears as '55', and the number of times this appears determines the number: 1 =
    # pair, 2 = 3 of kind, 4 = 4 of kind. Can make a statement to determine when two of one and one of another is
    # a full house.

print number_of_a_kind (["5S", "5D", "5D", "3C", "3H"])


def find_straight (hand):
    hand_no_suits = []
    for i in range (5):
        hand_no_suits += (hand[i])[0]
    hand_no_suits.sort()

    if ord(hand_no_suits[0]) >= ord("A") or ord(hand_no_suits[1]) >= ord("A") or ord(hand_no_suits[2]) >= ord("A") or ord(hand_no_suits[3]) >= ord("A") or ord(hand_no_suits[4]) >= ord("A"):
        #run the straight function for face cards.

#    elif int(hand_no_suits[0]) + 1 == int(hand_no_suits[1]) and int(hand_no_suits[1]) + 1 == int(hand_no_suits[2]) and int(hand_no_suits[2]) + 1 == int(hand_no_suits[3]) and int(hand_no_suits[3]) + 1 == int(hand_no_suits[4]):
        return 5

    else:
        return 0


# This function is only working for number cards, will have to write a separate function to include face cards...

def find_straight_face_cards (hand):  # either reference this in the function above or insert it there.
    hand_no_suits = []
    for i in range (5):
        hand_no_suits += (hand[i])[0]
    hand_no_suits.sort()



print find_straight_face_cards(["JS", "5D", "KD", "3C", "TH"])


# Put these two functions into the overall function of rankpokerhand, and add an if statement based on whether there
# are face cards or not. If there are, make it run find_straight_face_cards; if no face cards, use
# find_straight_num_cards.


# If statement to run face cards: use an if statement that compares the ord() of the value to between a certain range,
# and then do an or statement to run that same comparison for every other item in the hand_no_suits list. If any of
# them fall into that proper range, then the hand must include a face card.


# A, J, K, Q, T

def new_letter_to_number (letter):
    hand_list = []
    if ord(letter) == ord("A"):
            hand_list += [ord(letter) - ord("A") + 13] # This +14 is to make an A be a 14, same for the lines below...
    elif ord(letter) == ord("J"):
            hand_list += [ord(letter) - ord("J") + 10]
    elif ord(letter) == ord("K"):
            hand_list += [ord(letter) - ord("K") + 12]
    elif ord(letter) == ord("Q"):
            hand_list += [ord(letter) - ord("Q") + 11]
    elif ord(letter) == ord("T"):
            hand_list += [ord(letter) - ord("T") + 9]
    else:
        pass
    return hand_list


print new_letter_to_number("T")

# This function above was to turn all of the face cards into numbers, progressing from 2 to 14. Then, I could
# implement the same method as above for teh number cards to check for a straight....This may be too complicated and
# time consuming. It would also probably be good to use the functions that he described for this.

# The function is definitely not working right. Instead of returning these values, it should replace these values back
# into the given list. That may be complicated...

def find_full_house (hand):
    string_of_ranks = string_ranks(hand)
    full_house = 0
    for i in range(0, 13):
        if string_of_ranks[i] <= 1:
            full_house += 0
    for I in range (0, 13):
        full_house +=1
    return full_house

# ^^ Scrapped this function