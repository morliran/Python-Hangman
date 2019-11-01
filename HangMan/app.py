from player import Player
from level import Level
from word import Word
from game import Game

j, difficulty = 1, 0
p = Player("abc", "123")
while j > 0:
    while True:
        print("Choice level")
        print("1 -> Easy")
        print("2 -> Medium")
        print("3 -> Hard")
        difficulty = int(input("Level: "))
        if 1 <= difficulty <= 3:
            break
    l1 = Level(difficulty)
    rand_word = l1.choose_word(difficulty)
    w = Word(rand_word, l1)
    g = Game(p, w)
    print(f"The word contains {len(w.get_word())} letters")
    g.show_hint()
    while g.has_guess() and not g.get_win() and w.get_enable():
        print("If you need another hint press on key 1")
        ch = input("Give me char: ").lower()  # If needed change the input string to lower case string
        # Here ch[0] -> represent the first char of the input string
        if ch[0] == '1':
            g.show_hint()
        else:
            g.make_guess(ch[0])
    j = 0


