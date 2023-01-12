class Player:
    # Метод __init__ является конструктором для класса и принимает в качестве одного аргумента "name".
    # Он устанавливает переменную экземпляра "name" на переданное имя и создает пустой набор "слов", которые будет использовать игрок.
    def __init__(self, name):
        self.name = name
        self.words = set()

    # Метод add_word принимает слово и добавляет его к набору слов, используемых игроком.
    def add_word(self, word):
        self.words.add(word)

    # Метод was_used принимает слово и проверяет, существует ли оно в наборе слов, используемых игроком.
    def was_used(self, word):
        return word in self.words

    # Метод get_word_count возвращает количество слов, использованных игроком.
    def get_word_count(self):
        return len(self.words)

    # Метод __repr__ возвращает строковое представление экземпляра проигрывателя. Этот метод используется для печати класса.
    def __repr__(self):
        return f'Player(name={self.name}, words={self.words})'
