import random
import os
import time

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def bets():
    w = False
    while w is not True:
        set_wag = int(input(('money: {p_money}\n\nwager          |MIN:1 MAX:100|\n1)0.3 \n2)0.5 \n3)1 \n4)5 \n5)10 \n6)25 \n7)100 \n'.format(p_money=p.p_money))))
        if set_wag == 1:
            p.p_wager = 0.3
            print('low value')
            w = False
        elif set_wag == 2:
            p.p_wager = 0.5
            print('low value')
            w = False
        elif set_wag == 3:
            p.p_wager = 1
            w = True
        elif set_wag == 4:
            p.p_wager = 5
            w = True
        elif set_wag == 5:
            p.p_wager = 10
            w = True
        elif set_wag == 6:
            p.p_wager = 25
            w = True
        elif set_wag == 7:
            p.p_wager = 100
            w = True 


def reset_cards():
    d.d_cards = [cards(), cards()]
    p.p_cards = [cards(), cards()]


def main():
    print('          dealer\n           {d_cards}\n'.format(d_cards=d.d_cards))
    print('          player\n          {p_cards}\n MONEY: {p_money}               WAGERED: {p_wager}'.format(p_cards=p.p_cards, p_money=p.p_money, p_wager=p.p_wager))


def cards():
    two_to_teen = [2, 3, 4, 5, 6, 7, 8, 9]
    ace = [1]
    jack = [10]
    king = [10]
    queen = [10]
    deck_cards = ace + two_to_teen + jack + king + queen
    random_cards = deck_cards[random.randint(0, len(deck_cards)-1)]
    return random_cards


def buy():
    return cards()


class Dealer(object):
    def __init__(self, d_cards, d_money, d_wager): 
        self.d_cards = d_cards
        self.d_money = d_money
        self.d_wager = d_wager
d = Dealer([], 100, 0)

class Player(object):
    def __init__(self, p_cards, p_money, p_wager):
        self.p_cards = p_cards
        self.p_money = p_money
        self.p_wager = p_wager
p = Player([], 100, 0)

clear()

bets()

clear()

reset_cards()
while True:
    main()

    game_resp = int(input(('(1)buy (2)stop ')))
    if game_resp == 1:
        p.p_cards.append(buy())
        clear()
    elif game_resp == 2:
        while (21-(sum(d.d_cards))) >= 5:
            d.d_cards.append(buy())
        else:
            print(main())
            pass

        if sum(p.p_cards) <= 21 and sum(p.p_cards) > sum(d.d_cards):
            print('YOU WIN')
            p.p_money += p.p_wager*2
            reset_cards()
            time.sleep(3)
            clear()
            bets()
        elif sum(d.d_cards) <= 21 and sum(d.d_cards) > sum(p.p_cards) :
            print('DEALER WIN')
            reset_cards()
            time.sleep(3)
            p.p_money -= p.p_wager
            clear()
            bets()
        #if it exceed the value
        elif(sum(p.p_cards))-21 < (sum(d.d_cards))-21:
            print('YOU WIN')
            p.p_money += p.p_wager*2
            reset_cards()
            time.sleep(3)
            clear()
            bets()
        elif (sum(d.d_cards))-21 < (sum(p.p_cards))-21:
            print('DEALER WIN')
            reset_cards()
            time.sleep(3)
            p.p_money -=  p.p_wager
            clear()
            bets()

    if p.p_money <= 0.3:
        print('your money is over!')
        break

