class BasicWord:
    # Метод __init__ является конструктором для класса и принимает два аргумента: "word" и "вложенные слова".
    # Он устанавливает переменную экземпляра "word" для переданных слов и создает набор "слов" из переданного списка.
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = set(subwords)

    # Метод has_subword принимает слово и проверяет, существует ли оно в наборе вложенных слов для базового экземпляра Word.
    def has_subword(self, word):
        return word in self.subwords

    # Метод get_word_count возвращает количество вложенных слов для базового экземпляра Word.
    def get_word_count(self):
        return len(self.subwords)

    # Метод __repr__ возвращает строковое представление экземпляра базовой формы . Этот метод используется для печати класса.
    def __repr__(self):
        return f'Basicword(word={self.word}, subwords={self.subwords})'
