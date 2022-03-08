# RPSLS (Rock, Paper, Scissors, Lizard, Spock)

Learning Objective

Using the concepts of OOP by creating classes and using objects (instances of those classes) to interact with each other, create a console version of the classic game Rock Paper Scissors Lizard Spock.

Technologies

Python, Visual Studio Code w/ Debugger, Git/GitHub

Before You Begin

Be sure to refer to the framework document for setup steps before starting to code!

User Stories

Total Unweighted Project Points: /65

Total Weighted Project Points: /20

As a developer, I want to make at least 10 commits with descriptive messages.

 As a developer, I want to find a way to properly incorporate inheritance into my game.

As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.

 As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).

NOTE: Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!

As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!

 As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.

As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.

## Our Compare Gestures Fuc alt. Solutions

```
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

        p1 = player.gestures.index(gest1)
        p2 = player.gestures.index(gest2)
        print()
        if (p1 + 1) % 3 == p2:
            return "Player 2 won"
        elif p1 == p2:
            return "It is a draw"
        else:
            return "Player 1 won"
```