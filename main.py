
from basic_word import BasicWord
from player import Player
from utils import load_random_word


def main():
    user_input = input("Ввведите имя игрока: ")                        #Переменная user_input устанавливается на ввод от пользователя, который является его именем.

    player = Player(user_input)                                        #Новый экземпляр класса "Player" создается с именем пользователя и присваивается переменной "player".
    print(f"Привет {user_input}")

    word, subwords = load_random_word()                                #Функция "load_random_word" вызывается для получения случайного слова и его подслов,
    basic_word = BasicWord(word, subwords)                             #которые затем используются для создания экземпляра класса "BasicWord" и присваиваются переменной "basic_word".
    word_count = basic_word.get_word_count()                           #Переменная word_count установлена на количество вложенных слов для экземпляра "basic_word".

    print(f"Составьте {word_count} слова из слова {basic_word.word}")
    print(f"Слова должны быть не короче 3 букв")

    print(f"Чтобы закончить игру, угадайте все слова или напишите stop")
    print(f"Поехали, ваше первое слово?")

    for i in range(word_count):

        user_input = input()

        if user_input in ["stop", "стоп"]:
            break

        is_used = player.was_used(user_input)
        is_subword = basic_word.has_subword(user_input)

        if not is_used and is_subword:
            print(f"верно")
            player.add_word(user_input)
        else:
            print(f"неверно")

    words_ok = player.get_word_count()

    if words_ok == word_count:
        print(f"Поздравляю, вы угадали все {word_count} слов!")
    else:
        print(f"Попытки закончились, игра завершена! Вы угадали {words_ok} слов")


main()

