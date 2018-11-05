'''
This is a blackjack game of user agains computer
In This version there are no considuration of the cards type (Hart, Dymod, etc')
Need to Insert Player name it amount of mony and start to play.
computer will always add card if its less than 17
'''
import random

class Pac():
    def __init__(self):
        self.allcardsinpack = {1:4,2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 'J':4, 'Q':4, 'K':4, 'A':4 }
        self.pack = self.allcardsinpack

    def return_cards_in_pack(self):
        return self.pack
    
    def pull_card(self):
        # Getting random key from pack
        card  = random.choice(list(self.pack.keys()))
        # Reducing the card from the pack 
        self.pack[card] -= 1
        # Checking if its the last card from the same card number if yes remove it from dictunary - for more efficiant random
        if (self.pack[card] == 0):
            self.pack.pop(card)
        
        return card
            

class Player():

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        self.hand = []

    def value_hand(self):
        hand_val = 0
        for card in self.hand:
            if card == 'J' or card == 'Q' or card == 'K':
                hand_val += 10
            elif card == 'A':
                hand_val += 1
            else:
                hand_val += card
        
        return hand_val


    def deposit(self,val):
        self.balance += val
        #return f'Deposit Accepted - Account Balance: {self.balance}'
    
    def withdraw(self,val):
        if val <= self.balance:
            self.balance -= val
            return True
        else:
            return False


def get_check_int (text):
    while True:
        try:
            intval = int(input(text))
        
        except ValueError:
            print('Must be a number!')
            continue

        else:
            break
    
    return intval
        


mypack = Pac()

player_name = str(input('Please Enter your name: '))

while True:
    player_depo = get_check_int('Please Enter your Deposit: ')
    if player_depo <= 10000:
        break
    else:
        print('Maximum deposit is 10,000$')
        continue

# creating Player 1 Object
player1 = Player(player_name, player_depo)
#print(player1.name, player1.balance)

# Creating Computer Object
complayer = Player('Computer')

# Game on while True
while True:
    # Placing Bet - Bet Not OK while true,
    while True:
        player_bet = get_check_int('Please place your bet: ')
        if player_bet <= player1.balance:
            player1.balance -= player_bet
            break

        else:
            print('Your balance is lower than the bet!')
            continue

    player1.hand.append(mypack.pull_card())
    player1.hand.append(mypack.pull_card())
    print(player1.name, player1.balance, player1.hand, player1.value_hand())
    
    complayer.hand.append(mypack.pull_card())
    complayer.hand.append('X')
    print(complayer.name, complayer.balance, complayer.hand)

    # Player 1 pool from Pac while True
    while True:
        if player1.value_hand() <= 21:
            move =  input('Do you want another card? Choose Y or N:')
            if move == 'Y' or move == 'y':
                player1.hand.append(mypack.pull_card())
                print(f'Hand: {player1.hand}. Hand Value is: {player1.value_hand()}')
                continue
            else:
                break
        else:
            print('Your hand is over 21. you lost.')
            break

    complayer.hand.remove('X')
    complayer.hand.append(mypack.pull_card())
    print(complayer.name, complayer.balance, complayer.hand, complayer.value_hand())
    
    while True:
        if player1.value_hand() <= 21 and complayer.value_hand() < player1.value_hand() and complayer.value_hand() < 17:
            complayer.hand.append(mypack.pull_card())
            print(complayer.name, complayer.balance, complayer.hand, complayer.value_hand())
            continue
        else:
            break
   
    if complayer.value_hand() > 21 or player1.value_hand() > complayer.value_hand() and player1.value_hand() <= 21:
        player1.deposit(player_bet*2)
        print(f'{player1.name} you won {player_bet*2}$ !!! Yor Balance now is {player1.balance}')
        
    elif player1.value_hand() == complayer.value_hand():
        print(f'{player1.name} your even with Computer. Yor Balance now is {player1.balance}')
        player1.deposit(player_bet)
    else:
        print(f'{player1.name} you lost {player_bet}$ !!! Yor Balance now is {player1.balance}')


    if input('Do you want to play again? Y or N:') == 'y':
        complayer.hand = []
        player1.hand = []
        continue
    else:
        break
        