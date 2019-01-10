import random

class Card:

    suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_name = [None, 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s' % (Card.rank_name[self.rank], Card.suit_name[self.suit])

    # def __lt__(self, other):
    #     #檢查花色
    #     if self.suit < other.suit:
    #         return True
    #     if self.suit > other.suit:
    #         return False
    #     #檢如果花色一樣，就檢查階級
    #     return self.rank < other.rank
    '''下面是改成元組的方式取比較
    '''
    def __lt__(self, other):
        t1 = self.suit, other.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        '''移除最後一張牌
        '''
        return self.cards.pop()
    
    def add_card(self, card):
        '''新增一張牌
        '''
        return self.cards.append(card)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label

def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        # print(type(obj).mro())
        if method_name in ty.__dict__:
            # print(ty.__dict__)
            return ty
    return None

card1 = Card(2, 11)
card2 = Card(3, 10)
print(card1)
print(card2)
print(card1 < card2)

deck = Deck()
# print(deck)
card = deck.pop_card()

hand = Hand('new hand')
print(hand.cards)
print(hand.label)
print(hand.add_card(card))
print(hand)

hand = Hand()
print(find_defining_class(hand, 'shuffle'))