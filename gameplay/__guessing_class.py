import json
import random
from time import sleep


class GuessingGame:

    """
    Class to play the guessing game
    """

    def __init__(self, type_of_game: str, possible_difficulties=('easy', 'standard', 'hard')):

        """
        Constructor of the class GuessingGame
        :param type_of_game: The type of game (integral or derivative)
        :param possible_difficulties: The possible difficulties of the game. Default: ('easy', 'medium', 'hard')
        """

        self.data = self.__load_data(type_of_game)
        self.difficulty = None
        self.__possible_difficulties = possible_difficulties
        self.score = {
            'correct': 0,
            'failed': 0
        }

    def __load_data(self, type_of_game: str) -> dict:

        """
        Method to load the data from the json file.
        :param type_of_game:
        :return:
        """
        with open(f'data/{type_of_game}.json', 'r') as file:
            self.data: dict = json.load(file)
        return self.data

    def get_random_category(self) -> str:

        """
        Method to get a random category of equations
        :return: A random category of equations
        """
        categories = list(self.data.keys())
        random_category = random.choice(categories)
        return random_category

    def get_random_equations(self, category: str) -> list:

        """
        Method to get 3 random equations from a category of equations
        :param category: The category of equations
        :return: A list of 3 random equations from the category
        """

        integrals = self.data[category]
        random_equations = random.choices(list(integrals), k=3)
        # Check if the 3 random equations are unique
        while len(set(random_equations)) != 3:
            random_equations = random.choices(list(integrals), k=3)

        return random_equations

    def get_random_equation(self, category: str) -> str:

        """
        Method to get a random equation from a category of equations
        Used for the easy and hard mode of the game
        :param category: The category of equations
        :return: A random equation from the category
        """

        integrals = self.data[category]
        random_equation = random.choice(list(integrals))
        return random_equation

    def start_game(self) -> bool:

        """
        Method to start the game
        :return: True if the user wants to continue playing, False otherwise
        """

        match self.difficulty:
            case 'easy':
                return self.__easy_mode()
            case 'standard':
                return self.__standard_mode()
            case 'hard':
                return self.__hard_mode()

    def __easy_mode(self) -> bool:
        """
        Play the easy difficulty mode of the game. You are given an equation and an integral, and you have to choose if it is the correct one or not
        :return: True if the answer is correct, False otherwise
        """
        category = self.get_random_category()
        correct_equation = self.get_random_equation(category)
        correct_answer = self.data[category][correct_equation]
        false_equation = self.get_random_equation(category)
        false_answer = self.data[category][false_equation]
        random_answer = random.choice([correct_answer, false_answer])

        print(f'Your score is: {self.score["correct"]}/{self.score["correct"] + self.score["failed"]}\n')
        print('Is this the correct answer? (y/n, write x for exit)')
        print('Equation: {}'.format(correct_equation))
        print('Answer: {}'.format(random_answer))

        try:
            choice = input('Is this the correct answer? (y/n, write x for exit): ')
            if choice.lower() == 'x' or choice.lower() == 'exit':
                return False
            else:
                if random_answer == correct_answer:
                    if choice.lower() == 'y':
                        self.score['correct'] += 1
                        print('Correct!')
                    else:
                        self.score['failed'] += 1
                        print('Incorrect! The correct answer was: {}'.format(correct_answer))
                else:
                    if choice.lower() == 'n':
                        self.score['correct'] += 1
                        print('Correct!')
                    else:
                        self.score['failed'] += 1
                        print('Incorrect! The correct answer was: {}'.format(correct_answer))

                sleep(1)
                return True

        except Exception as e:
            return self.__easy_mode()

    def __standard_mode(self) -> bool:

        """
        Play the standard difficulty mode of the game. This mode is not implemented yet
        ...
        :return: True if the answer is correct, False otherwise
        """
        category = self.get_random_category()
        equations = self.get_random_equations(category)
        answers = {i: equation for i, equation in enumerate(equations)}

        print(f'Your score is: {self.score["correct"]}/{self.score["correct"] + self.score["failed"]}\n')
        print('Which one is the correct answer?')
        print('Equation: {}'.format(equations[0]))
        for equation in answers:
            print('{}. {}'.format(equation + 1, self.data[category][answers[equation]]))
        try:
            choice = input('Which one is the correct answer? (1, 2 or 3. write x for exit): ')
            if choice.lower() == 'x' or choice.lower() == 'exit':
                return False
            else:
                if answers[int(choice) - 1] == equations[0]:
                    self.score['correct'] += 1
                    print('Correct!')
                else:
                    self.score['failed'] += 1
                    print('Incorrect! The correct answer was: {}'.format(self.data[category][equations[0]]))

                return True

        except Exception as e:
            return self.__easy_mode()

    def __hard_mode(self) -> bool:

        """
        Play the hard difficulty mode of the game. This mode is not implemented yet
        You have to write the whole equation as the answer
        :return: True if the answer is correct, False otherwise
        """

        category = self.get_random_category()
        correct_equation = self.get_random_equation(category)
        correct_answer = self.data[category][correct_equation]

        print(f'Your score is: {self.score["correct"]}/{self.score["correct"] + self.score["failed"]}\n')
        print('Write the answer for this equation: (write x for exit)')
        print('Equation: {}'.format(correct_equation))
        try:
            choice = input('Your answer: ')
            if choice.lower() == 'x' or choice.lower() == 'exit':
                return False
            else:
                if choice == correct_answer:
                    self.score['correct'] += 1
                    print('Correct!')
                else:
                    self.score['failed'] += 1
                    print('Incorrect! The correct answer was: {}'.format(correct_answer))


                return True

        except Exception as e:
            return self.__easy_mode()

    def valid_difficulty(self, difficulty: str) -> bool:

        """
        Check if the difficulty is valid
        :param difficulty: Difficulty to check
        :return: True if the difficulty is valid, False otherwise
        """

        if difficulty in self.__possible_difficulties:
            return True
        else:
            return False
