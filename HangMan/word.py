import random
from level import Level


class Word:
    def __init__(self, word, level):
        self.__hint = ''
        self.__enable = True
        self.__word = word
        self.__level = Level(level.get_value())

    def get_word(self):
        return self.__word

    def set_word(self, value):
        self.__word = value

    def get_hint(self):
        return self.__hint

    def set_hint(self):
        index = random.randint(0, len(self.get_word()) - 1)
        self.__hint = self.get_word()[index]

    def get_level(self):
        return self.__level

    def set_level(self, value):
        self.__level = value

    def get_enable(self):
        return self.__enable

    def set_enable(self, value):
        self.__enable = value

