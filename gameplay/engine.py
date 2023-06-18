from time import sleep

from . import __guessing_class


def run() -> None:

    """
    Function to run the game
    :return: None
    """

    while True:
        choice = input("Do you want to guess an integral or derivative? (i/d): ").lower()
        if choice not in ['i', 'd']: # If the user doesn't choose a valid option
            print('Invalid choice, try again') # print an error message and loop again
        else: # If the user chooses a valid option,
            match choice: # set the choice to the correct string
                case 'i':
                    choice = 'integral'
                case 'd':
                    choice = 'derivative'
            break # and break out of the loop

    game = __guessing_class.GuessingGame(choice) # Create a new instance of the game class

    while True: # Loop until the user chooses a valid difficulty
        choose_difficulty = input('Choose a difficulty (easy, standard, hard): ')
        if game.valid_difficulty(choose_difficulty) is True:
            game.difficulty = choose_difficulty # Set the difficulty to the user's choice
            break # and break out of the loop
        else: # If the user doesn't choose a valid difficulty
            print('Invalid difficulty, try again') # print an error message and loop again

    while True: # Loop until the user wants to exit the game
        continue_playing = game.start_game() # Start the game and set continue_playing to the return value
        if continue_playing is False: # If the user wants to exit the game
            break

    print('Thanks for playing!')

    sleep(2) # Wait 2 seconds before closing console
