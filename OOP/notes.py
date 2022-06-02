# #BASICS // ATTRIBUTES
# #//////(1)
# class Dog():
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
# mydog = Dog("pitbull", 'bagira')
# print(mydog.breed)
# print(mydog.name)
#
# #//////(2)

#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
suits = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("creating New Ordered Deck!")
        self.all_cards = [(s,r) for s in suits for r in ranks]

        # for suit in suits:
        #     for rank in ranks:
        #         self.all_cards.append(Card(suit,rank))

    def shuffle_it(self):
        print("Shuffling Deck!")
        shuffle(self.all_cards)

    def split_in_half(self):
        return (self.all_cards[:26], self.all_cards[26:])



class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_card(self,added_cards):
        self.cards.extend(added_cards)
        # self.values += values[card.rank]

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

new_deck = Deck()
new_deck.shuffle_it()
half1, half2 = new_deck.split_in_half()

comp  = Player("computer",Hand(half1))

name = input("Please, Enter your name:")
human = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while human.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round:")
    print(human.name + " has the count: " + str((len(human.hand.cards))))
    print(comp.name + " has the count: " + str((len(comp.hand.cards))))
    print("Play a game!")
    print("\n")

    table_cards = []

    #Play cards
    c_card = comp.play_card()
    h_card = human.play_card()

    #Add to table_cards
    table_cards.append(c_card)
    table_cards.append(h_card)

    if c_card[1] == h_card[1]:
        war_count += 1

        print("WAR!")

        table_cards.extend(human.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        #player_cards
        c_card = comp.play_card()
        h_card = human.play_card()

        #add to the table
        table_cards.append(c_card)
        table_cards.append(h_card)

        if ranks.index(c_card[1]) < ranks.index(h_card[1]):
            human.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)
    else:
        if ranks.index(c_card[1]) < ranks.index(h_card[1]):
            human.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)
print("GAME OVER!")
print("It lasted {} rounds:".format(str(total_rounds)))
print("A war has happened: " + str(war_count) + "times")

if comp.still_has_cards() == True:
    print("Computer Wins!!!!")
    print("Comp has : {}".format(str(len(comp.hand.cards))))
else:
    print("Human user Wins!!!!")
    print("Human user has : {}".format(str(len(human.hand.cards))))

# Use the 3 classes along with some logic to play a game of war!
