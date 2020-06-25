# BlackJack
Blackjack ou 21 e um jogo de cassino que pode ser jogado de 1 a 8 pessoas, que o objetivo e ter mais pontos que o adversario sem ultrapassar 21.

obs:codigo feito em ingles.

## Como o codigo funciona

### apostas
A funcao bets serve para informar o valor da aposta.
muitas mesas de cassino estabelecem um maximo e um minimo de apostas.
```python
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
```
### dando as cartas
a funcao como proprio nome diz dara cartas aleatorias para os jogadores.
```python
def cards():
    two_to_teen = [2, 3, 4, 5, 6, 7, 8, 9]
    ace = [1]
    jack = [10]
    king = [10]
    queen = [10]
    deck_cards = ace + two_to_teen + jack + king + queen
    random_cards = deck_cards[random.randint(0, len(deck_cards)-1)]
    return random_cards
```
### jogadores
os jogadores no caso o dealer(maquina) e voce. Foi utilizado POO na criacao, tanto pra facilitar a configuracao de dinheiro, valor de aposta e cartas quanto na exigencia do professor.
```python
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
```
### ganhou ou perdeu.
primeira parte feita pro jogador comprar suas cartas.

segunda parte pro dealer(maquina) comprar tabem suas cartas e ao final saber quem esta mais perto do 21 e quem tem a soma de cartas maior.
```python
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
```
