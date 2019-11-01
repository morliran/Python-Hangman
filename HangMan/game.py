from word import Word
from player import Player


class Game:
    def __init__(self, player, word):
        self.__player = Player(player.get_name(), player.get_password())
        self.__win = False
        self.__word = Word(word.get_word(), word.get_level())
        self.__enable = True
        self.__guess = 6
        self.__p_word = [None] * len(word.get_word())  # Initialize an empty list with the same size as the secret word

    def get_word(self):
        return self.__word

    def set_word(self, word):
        self.__word = word

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player

    def get_win(self):
        return self.__win

    def set_win(self, win):
        self.__win = win

    def get_guess(self):
        return self.__guess

    def set_guess(self, guess):
        self.__guess = guess

    def has_guess(self):
        if self.get_guess() > 0:
            return True
        return False

    def check_win(self):
        i, size = 0, len(self.__word.get_word())
        flag = True
        for i in range(size):
            if self.__p_word[i] == 0 or self.__guess == 0:
                self.set_win(False)
                if self.__guess == 0:
                    print("Sorry you lost, please try again")
                    print(f"The word was: {self.__word.get_word()}")
                return
        if len(self.__p_word) == size and not self.__p_word.__contains__(None):
            self.set_win(True)
            print("Congratulation you won")
            print(f"Total coins at finish: {self.__player.get_coins()}")
            self.__word.set_enable(False)
        return

    def make_guess(self, c):
        i, found = 0, False
        temp = list(self.__word.get_word())  # Convert the secret word to a list so I can iterate over each char in her
        for i in range(len(self.__p_word)):
            if temp[i] == c:  # If the char is presented in the secret word
                found = True
                if self.__p_word[i] != c:  # Checking if the char is not existing already in the reveling list
                    self.__p_word[i] = c
                    self.__player.add_coins()
        if not found:  # If the guessing character is not present in the secret word
            self.__guess -= 1
            print(f"Total guess left = {self.get_guess()}")
        for i in range(len(self.__p_word)):
            if self.__p_word[i] is None:  # Printing all none value as underscore( _ ) char
                print("_ ", end='')
            else:
                print(f" {self.__p_word[i]} ", end='')  # Override underscore char by the correct reveling char
        print()
        self.check_win()

    def show_hint(self):
        while True:  # Making sure adding hitting character that are not already presented in the reveling list
            self.__word.set_hint()
            if not self.__p_word.__contains__(self.__word.get_hint()):
                self.make_guess(self.__word.get_hint())  # Sending hinting character to the guessing method
                self.__player.set_coins(self.__player.get_coins() - 15)
                break
