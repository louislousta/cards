import random



def init_deck(): # Returns a list of 52 card tuples 
        deck = []
        for val in range(13):
            for suit in range(4):
                card = (suit,val)
                deck.append(card)

        return deck

def card_reader(c):    # reads a card and returns readable value e.g. KH or 4H
        suit = c[0]
        val = c[1]
        if (suit == 0):
            suit = 'H'
        elif (suit == 1):
            suit = 'D'
        elif (suit == 2):
            suit = 'C'
        elif (suit == 3):
            suit = 'S'
        if (val>9):
            if (val == 10):
                val = 'J'
            elif (val == 11):
                val = 'Q'
            elif (val == 12):
                val = 'K'
        elif (val == 0):
            val = 'A'
        else:
            val = str(val+1)
        card = val + suit
        return card

def shuffle(deck):  #randomise deck
        random.shuffle(deck)
        return deck

def deal(deck,hand_size): # returns a hand of cards
    hand = []
    for i in range(hand_size):
            hand.append(deck[i])
    return hand