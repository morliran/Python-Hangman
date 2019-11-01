STARTING_COINS = 100


class Player:
    def __init__(self, name, password):
        self.__coins = STARTING_COINS
        self.__name = name
        self.__password = password

    def get_coins(self):
        return self.__coins

    def set_coins(self, value):
        self.__coins = value

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_password(self, value):
        self.__password = value

    def get_password(self):
        return self.__password

    def add_coins(self):
        self.__coins += 15
