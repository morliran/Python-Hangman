import random


class Level:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    @staticmethod
    def __get_word(word_list):
        return word_list[random.randint(0, len(word_list) - 1)]

    def choose_word(self, level):
        word_arr = []
        if level == 1:
            word_arr = ["food", "drink", "car", "chair", "balloon", "spoon"]
        elif level == 2:
            word_arr = ["computer", "keyboard", "screen", "laptop", "server", "magnet"]
        elif level == 3:
            word_arr = ["algorithm", "statistics", "database", "management", "network", "object"]
        return self.__get_word(word_arr)
