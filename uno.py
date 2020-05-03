from cards import *
import random

def display_scene():
    print(f'{"*"*60}')
    print(f'Top card --> {game.top_card()}')
    print(f'{"-"*60}')
    print('Your cards --> ',end='')
    player.view_cards()
    print(player.cards_count)
    print(f'{"-"*60}')
    print('Comp cards --> ',end='')
    computer.view_cards()
    print(computer.cards_count)
    print(f'{"-"*60}')
    print(f'Cards in deck: {deck.cards_count}')
    print(f'{"*"*60}')


def computer_play(card,deck,game,color,player):
    for c in computer.cards:
        result = computer.throw(c.name,game,color)
        if result !=0:
            game.cards_stack.append(result)
            turn = evaluate(game.top_card(),deck,computer,player)
            turn = 1 if turn == 0 else 0
            return turn
    computer.pick(deck)
    print('Computer picks a card')
    turn = 0
    return turn

def evaluate(card,deck,player1,player2):

    turn = 1 # 0 -> for player1 and 1 -> for player2
    global color
    # Wild
    if card.name[0] == 'W':
        if player1.name != 'Computer':
            col = input('Change color to :  ')
            while col not in 'RGBY':
                print('Invalid color')
                col = input('Change color to :  ')
            color = col
        else:
            color = random.choice(['R','G','B','Y'])
            print(f'Computer has changed color to {color}')
        turn = 1
   
    # Reverse
    elif card.name[1] == 'R':
        turn = 1

   # Draw2
    elif card.name[1] == 'D':
        for card in deck.deal(2):
            player2.cards.append(card)
        player2.cards_count += 2
        turn = 0
    
    # Draw4
    elif card.name[0] == 'D':
        for card in deck.deal(4):
            player2.cards.append(card)
        player2.cards_count += 4
        if player1.name != 'Computer':
            col = input('Change color to :  ')
            while col not in 'RGBY':
                print('Invalid color')
                col = input('Change color to :  ')
            color = col
        else:
            color = random.choice(['R','G','B','Y'])
            print(f'Computer has changed color to {color}')
        turn = 0

    # Skip
    elif card.name[1] == 'S':
        turn = 0

    return turn

color = None


# Initializing the player
player = input('Enter your name: ')
player = Player(player)
print(f'Welcome, {player}')

# Initializing the computer
computer = Player('Computer')

# Initialize the deck of cards
deck = Deck()
deck.shuffle()

# Dealining cards to the player and computer
player.cards = deck.deal(7)
computer.cards = deck.deal(7)

# Dealing the start card onto the staging area
game = Game()
game.cards_stack = deck.deal(2,True)

# player.view_cards()
# computer.view_cards()
# print(deck.cards_count)
# print(game.top_card())

# players = []
# players.append(player)
# players.append(computer)

turn = 0
color = game.top_card().name[0]

while True:


    valid = 0
    while not valid:
        display_scene()
        print('What do you wanna do?')
        print('1. Draw a card\n2. Play a card')
        option = input()
        if option == '1':
            player.pick(deck)
            valid = 1
            turn = 1
        elif option == '2':
            c = input('Which card? (0 to go back) :  ')
            if player.has(c):
                game.cards_stack.append(player.throw(c,game,color))
                if game.top_card() == 0:
                    game.cards_stack.remove(0)
                    print('\nInvalid move, cannot play that card\n')
                    continue
                player.view_cards()
                valid = 1
            else:
                print('You dont have that card')
                continue
        else:
            print('\nPrint invalid option\n')
            continue


    # display_scene()
    
    if player.cards_count ==0:
        print(f'Congrats {player.name} you have won')
        break
    
    if turn == 0:
        turn = evaluate(game.top_card(),deck,player,computer)
    
    while turn:
        turn = computer_play(game.top_card(),deck,game,color,player)
        if computer.cards_count ==0:
            print(f'Sadly {computer.name} has won')
            break

    
    
