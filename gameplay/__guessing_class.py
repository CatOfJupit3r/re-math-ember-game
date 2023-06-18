import json
import random


class GuessingGame:

    """
    Class to play the integral guessing game
    """

    def __init__(self, type_of_game: str = 'integral', possible_difficulties=('easy', 'medium', 'hard')):
        if possible_difficulties is None:
            possible_difficulties = ['easy', 'medium', 'hard']
        self.data = self.__load_data(type_of_game)
        self.difficulty = None
        self.__possible_difficulties = possible_difficulties
        self.score = {
            'correct': 0,
            'failed': 0
        }

    def __load_data(self, type_of_game: str) -> dict:
        with open(f'data/{type_of_game}.json', 'r') as file:
            self.data: dict = json.load(file)
        return self.data

    def get_random_category(self) -> str:
        categories = list(self.data.keys())
        random_category = random.choice(categories)
        return random_category

    def get_random_equations(self, category) -> list:
        integrals = self.data[category]
        random_equations = random.choices(list(integrals), k=3)
        return random_equations

    def start_game(self) -> bool:
        match self.difficulty:
            case 'easy':
                return self.__easy_mode()
            case 'medium':
                return self.__medium_mode()
            case 'hard':
                return self.__hard_mode()

    def __easy_mode(self) -> bool:
        category = self.get_random_category()
        equations = self.get_random_equations(category)
        answers = {i: equation for i, equation in enumerate(equations)}

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

                print(f'Your score is: {self.score["correct"]}/{self.score["correct"] + self.score["failed"]}\n')

                return True

        except Exception as e:
            return self.__easy_mode()

    def __medium_mode(self) -> bool:

        """
        Play the medium mode of the game. This mode is not implemented yet
        ...
        :return: True if the answer is correct, False otherwise
        """
        return False

    def __hard_mode(self) -> bool:

        """
        Play the hard mode of the game. This mode is not implemented yet
        You have to write the whole equation as the answer
        :return: True if the answer is correct, False otherwise
        """

        return False

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
