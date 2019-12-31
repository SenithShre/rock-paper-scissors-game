# Made by SenithShre
# Git hub: https://github.com/SenithShre

import random

def game():

    print('Welcome to Rock, Paper, Scissors Game')
    print('To play, type "Play"')
    user_input = input(': ')

    if user_input == 'Play':
        print('Rock, Paper, Scissors, Shoot!')
        user_input2 = input(': ')

        # If the user input is == to 'Rock'

        if user_input2 == 'Rock':
            answers = ('Rock', 'Paper', 'Scissors')
            final = random.choice(answers)
            print(final)

            # If random list is == to 'Rock'

            if final == 'Rock':
                print('Oh, it is a tie, would you like to play again? Y/N') # Prompts the user to play again
                user_input_tie = input(': ')

                # If the user input is == to Y, then the user can replay the game

                if user_input_tie == 'Y':
                    game()

                # If the user input is anything else, then the game will completley end

                else:
                    game == False

            # If random list is == to 'Paper'

            elif final == 'Paper':
                print('You lost, would you like to play again? Y/N')
                user_input_tie = input(': ')

                if user_input_tie == 'Y':
                    game()

                else:
                    game == False
            else:
                game == False

            # If the random list == to 'Scissors'

            if final == 'Scissors':
                print('You won, would you like to play again? Y/N')
                user_input_tie = input(': ')

                if user_input_tie == 'Y':
                    game()

                else:
                    game == False
            else:
                game == False

        # If the user input is == to 'Paper'

        if user_input2 == 'Paper':
            answers = ('Rock', 'Paper', 'Scissors')
            final = random.choice(answers)
            print(final)

            # If random list is == to 'Rock'

            if final == 'Rock':
                print('Oh, you won, would you like to play again? Y/N') # Prompts the user to play again
                user_input_tie = input(': ')

                # If the user input is == to Y, then the user can replay the game

                if user_input_tie == 'Y':
                    game()

                # If the user input is anything else, then the game will completley end

                else:
                    game == False

            # If random list is == to 'Paper'

            elif final == 'Paper':
                print('It is a tie, would you like to play again? Y/N')
                user_input_tie = input(': ')

                if user_input_tie == 'Y':
                    game()

                else:
                    game == False
            else:
                game == False

            # If the random list == to 'Scissors'

            if final == 'Scissors':
                print('You lost, would you like to play again? Y/N')
                user_input_tie = input(': ')

                if user_input_tie == 'Y':
                    game()

                else:
                    game == False
            else:
                game == False

        # If the user input is == to 'Scissors'

        if user_input2 == 'Scissors':
            answers = ('Rock', 'Paper', 'Scissors')
            final = random.choice(answers)
            print(final)

            # If random list is == to 'Rock'

            if final == 'Rock':
                print('Oh, you lost, would you like to play again? Y/N') # Prompts the user to play again
                user_input_tie = input(': ')

                # If the user input is == to Y, then the user can replay the game

                if user_input_tie == 'Y':
                    game()

                # If the user input is anything else, then the game will completley end

                else:
                    game == False

            # If random list is == to 'Paper'

            elif final == 'Paper':
                print('You won, would you like to play again? Y/N')
                user_input_tie = input(': ')

                if user_input_tie == 'Y':
                    game()

                else:
                    game == False
            else:
                game == False

            # If the random list == to 'Scissors'

            if final == 'Scissors':
                print('It is a tie, would you like to play again? Y/N')
                user_input_tie = input(': ')

                if user_input_tie == 'Y':
                    game()

                else:
                    game == False
            else:
                game == False

        else:
            print('Invalid Option')
            print('Would you like to restart? Y/N')
            user_input_restart = input(': ')

            if user_input_restart == 'Y':
                game()

            elif user_input_restart == 'N':
                print('Thanks for playing!')
                game == False

    else:
        print('Invalid Option')
    
game()
