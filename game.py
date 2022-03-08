from player import Player
from human import Human
from ai import Ai
player = Player()


class Game:
    def __init__(self):
        pass

    def run_game(self):
        # self.show_greeting()
        single_player = self.is_single_player_true()
        player_one_score = 0
        player_two_score = 0
        if single_player == True:
            player_one = Human()
            player_two = Ai()
        else:
            player_one = Human()
            player_two = Human()
        while player_one_score < 2 and player_two_score < 2:
            winner = self.compare_gestures(player_one.choose_gesture('Player One'), player_two.choose_gesture())
            if winner == 'Player 1 won':
                player_one_score += 1
            elif winner == 'Player 2 won':
                player_two_score += 1
            print(f'{winner} for this round!!')
        self.display_winner(player_one_score, player_two_score)
            
          
    def show_greeting(self):
        print('Welcome to rock, paper, scissors with a twist!\n')
        print('We added two more choices:\nLizard and Spock\n\n')
        print('Here are the rules:\n')
        print("Scissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n(and as it always has) Rock crushes Scissors")
        

    def is_single_player_true(self):
        player_choice = ''
        while player_choice != '1' and player_choice != '2':
            player_choice = input('Please enter "1" for a single player game, or "2" for a multi player game:')
            if player_choice != '1' or player_choice != '2':
                print('Please enter correct value')
        if player_choice == '1':
              return True
        else: return False            


    def compare_gestures(self, gest1, gest2):
        if gest1 == gest2:
            return "It is a draw"
        elif gest1 == 'rock' and (gest2  == 'scissors' or gest2  == 'lizard'):
            return "Player 1 won"  
        elif gest1 == 'paper' and   (gest2 == 'rock' or gest2  == 'spock'):
            return "Player 1 won"
        elif gest1 == 'scissors' and  (gest2 == 'paper' or gest2  == 'lizard'):
            return "Player 1 won"
        elif gest1 == 'lizard' and   (gest2 == 'spock' or gest2  == 'paper'):
            return "Player 1 won"
        elif gest1 == 'spock' and  (gest2 == 'scissors' or gest2  == 'rock'):
            return "Player 1 won"
        else: return "Player 2 won"    

        # p1 = player.gestures.index(gest1)
        # p2 = player.gestures.index(gest2)
        # print()
        # if (p1 + 1) % 3 == p2:
        #     return "Player 2 won"
        # elif p1 == p2:
        #     return "It is a draw"
        # else:
        #     return "Player 1 won"

        
    def display_winner(self, player_one_score, player_two_score):
        if player_one_score > player_two_score:
            print('Player One Wins the Game!')
        else:
            print('Player Two Wins the Game!')
        


    
   
