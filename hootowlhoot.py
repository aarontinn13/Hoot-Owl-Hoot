import random
import math

class Player():

    def __init__(self):
        self._hand = []



    def get_cards(self):
        while len(self._hand) != 3:
            self._hand.append(deck.pop())
        return self._hand

    def show_cards(self):
        return self._hand

    def play_card(self):
        if 'Sun' in self.show_cards():
            self._hand.remove('Sun')
            gameboard.advance_sun()
        else:
            card_to_play, owl_to_move, start, end = self.decision()
            self._hand.remove(card_to_play)
            gameboard.mark_board(end, owl_to_move)
            gameboard.unmark_board(start, owl_to_move)
            for i in owls:
                if i.owl_name() == owl_to_move:
                    i.change_position(end)
                    break

    def decision(self):
        '''figures out optimal solution (card, owl, owl start, owl end)'''
        list_of_owls = [(i.current_position(), i.owl_name()) for i in owls]
        owl_to_move = min(list_of_owls)
        list_of_moves = []
        for i in self.show_cards():
            for j in range(owl_to_move[0]+1,len(gameboard.show_board())):
                if gameboard.show_board()[j] == [i]:
                    list_of_moves.append((j,i))
                    break
                if gameboard.show_board()[j] == ['Nest'] or gameboard.show_board()[j][0] == 'Nest':
                    list_of_moves.append((39, i))
        return max(list_of_moves)[1],owl_to_move[1],owl_to_move[0],max(list_of_moves)[0]

class Board():

    def __init__(self):
        self._board = [['Yellow'],['Green'],['Orange'],['Blue'],['Purple'],['Red'],['Blue'],['Purple']
                        ,['Red'],['Yellow'],['Green'],['Blue'],['Orange'],['Red'],['Purple'],['Yellow']
                        ,['Green'],['Orange'],['Blue'],['Purple'],['Red'],['Green'],['Yellow'],['Orange']
                        ,['Blue'],['Purple'],['Red'],['Yellow'],['Green'],['Blue'],['Orange'],['Red']
                        ,['Purple'],['Yellow'],['Green'],['Blue'],['Orange'],['Red'],['Purple'],['Nest']]
        self._sun = 0

    def show_board(self):
        '''return current state of the board'''
        return self._board

    def show_suncount(self):
        '''returns current count of suns'''
        return self._sun

    def advance_sun(self):
        '''increment sun count by however many suns a player has from Player.play_card()'''
        self._sun += 1
        return self._sun

    def mark_board(self,owl_position, owl_name):
        '''mark the board with name to indicate someone on that position.'''
        return self._board[owl_position].append(owl_name)

    def unmark_board(self,owl_position, owl_name):
        '''unmark the board with 0 to indicate someone not on that position.'''
        return self._board[owl_position].remove(owl_name)


class Owl():

    def __init__(self, position, name):
        self._position = position
        self._name = name

    def current_position(self):
        '''returns the current position of the owl'''
        return self._position

    def owl_name(self):
        '''returns the name of the owl'''
        return self._name

    def change_position(self, position):
        '''change the position of the owl'''
        self._position = position
        return self._position

class HOOTOWLHOOT():

    def startgame(self, *players_and_owls):
        global owls
        global deck
        '''creating the deck'''
        color_cards = ['Yellow', 'Green', 'Orange', 'Blue', 'Purple', 'Red'] * 6
        sun_cards = ['Sun'] * 14
        deck = color_cards + sun_cards
        players = [players for players in players_and_owls if isinstance(players, Player)]
        owls = [owls for owls in players_and_owls if isinstance(owls, Owl)]
        random.shuffle(deck)

        for i in owls:
            gameboard.mark_board(i.current_position(),i.owl_name())

        Flag = True
        Win = 'No'

        while Flag:
            for i in players:
                i.get_cards()
                i.play_card()
                if gameboard.show_suncount() == 13:
                    Flag = False
                    break
                if len(gameboard.show_board()[-1]) == len(owls)+1:
                    Flag = False
                    Win = 'Yes'
                    break
        if Win == 'Yes':
            return 'Yes'
        else:
            return 'No'


count_of_wins_scenario = 0

for i in range(10000):
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()
    owl1 = Owl(0, 'owl1')
    owl2 = Owl(1, 'owl2')
    owl3 = Owl(2, 'owl3')
    owl4 = Owl(3, 'owl4')
    owl5 = Owl(4, 'owl5')
    owl6 = Owl(5, 'owl6')
    gameboard = Board()
    game = HOOTOWLHOOT()

    #enter arbitrary number of players 2-4 or owls 3-6
    if game.startgame(player1, player2, player3, player4, owl1, owl2, owl3, owl4, owl5, owl6) == 'Yes':
        count_of_wins_scenario += 1


win_probability = count_of_wins_scenario/10000
standard_deviation = math.sqrt(win_probability*(1-win_probability)/10000)

print(win_probability)
print(float(standard_deviation))


'''
Two Players, Three Owls
Win Probability: .9894
Standard Deviation: .0010240917927607882
Two Players, Six Owls
Win Probability: .6779
Standard Deviation: .004672810610328649
Four Players, Three Owls
Win Probability: .9541
Standard Deviation: .0020926822501278123
Four Players, Six Owls
Win Probability: .3973
Standard Deviation: .004893390542354044
'''
