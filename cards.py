import random

class Card:

    name = None
    pic = None

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

class Deck:
    
    initial_cards = [
            'R0','Y0','G0','B0',
            'R1','Y1','G1','B1',
            'R1','Y1','G1','B1',
            'R2','Y2','G2','B2',
            'R2','Y2','G2','B2',
            'R3','Y3','G3','B3',
            'R3','Y3','G3','B3',
            'R4','Y4','G4','B4',
            'R4','Y4','G4','B4',
            'R5','Y5','G5','B5',
            'R5','Y5','G5','B5',
            'R6','Y6','G6','B6',
            'R6','Y6','G6','B6',
            'R7','Y7','G7','B7',
            'R7','Y7','G7','B7',
            'R8','Y8','G8','B8',
            'R8','Y8','G8','B8',
            'R9','Y9','G9','B9',
            'R9','Y9','G9','B9',
            'RS','YS','GS','BS',
            'RS','YS','GS','BS',
            'RR','YR','GR','BR',
            'RR','YR','GR','BR',
            'RD2','YD2','GD2','BD2',
            'RD2','YD2','GD2','BD2',
            'W','W','W','W',
            'D4','D4','D4','D4',
            ]

    cards = []
    cards_count = 0

    def __init__(self):
        for card in self.initial_cards:
            c = Card(card)
            self.cards.append(c)
            self.cards_count += 1

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,count,start=False):
        dealt_cards = []
        restricted_cards = [
            'RS','YS','GS','BS',
            'RR','YR','GR','BR',
            'RD2','YD2','GD2','BD2',
            'W','D4'
                ]

        if start:
            card = random.choice(self.cards)
            while card  in restricted_cards:
                card = random.choice(self.cards)
            dealt_cards.append(card)
            self.cards.remove(card)
            self.cards_count -= 1

        else:
            for i in range(count):
                card = random.choice(self.cards)
                dealt_cards.append(card)
                self.cards.remove(card)
                self.cards_count -= 1

        return dealt_cards

    def display(self):
        for card in self.cards:
            print(card.name,end='   ')
        print()


class Player:

    name = None
    cards = []
    cards_count = 7

    def __init__(self,name='Player'):
        self.name = name

    def __str__(self):
        return self.name

    def view_cards(self):
        for card in self.cards:
            print(card,end='   ')
        print()
    
    def has(self,card):
        for c in self.cards:
            if card == c.name:
                return True
        return False
            
    def throw(self,card,game,color):
        i = 0
        for c in self.cards:
            i +=1
            if card == c.name:
                if self.is_legal_move(card,game,color):
                    temp = c
                    self.cards.remove(c)
                    self.cards_count -=1
                    return temp
                else:
                    return 0

    def pick(self,deck):
        self.cards.append(deck.deal(1)[0])
        self.cards_count +=1
       

    def is_legal_move(self,card,game,color):
        # print(game.top_card().name)
        # print(card[0],card[1])
        try:
            if card[0] == 'W' or card[0] == color or card[0] == 'D' or card[0] == game.top_card().name[0] or card[1] == game.top_card().name[1]:
                return True
            else:
                return False
        except:
            pass
class Game:

    cards_stack = []
    direction = 1      #1 for clockwise and 0 for counter-clockwise


    def top_card(self):
        return self.cards_stack[-1]

