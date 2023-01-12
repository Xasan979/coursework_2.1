
import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
import random

def load_random_word():
    warnings.simplefilter('ignore', InsecureRequestWarning)  #Функция warnings.simplefilter используется для игнорирования предупреждений, вызванных использованием непроверенного SSL-сертификата при выполнении запроса API.
    url = 'https://jsonkeeper.com/b/X2ZK'
    response = requests.get(url, verify=False)               #Функция requests.get используется для выполнения запроса GET к конечной точке API, указанной в переменной url. Аргумент verify=False используется для игнорирования предупреждения, вызванного использованием непроверенного SSL-сертификата
    data = response.json()                                   #Функция response.json() используется для анализа данных JSON, возвращаемых API, в объект Python.
    random_word = random.choice(data)                        #Функция random.choice используется для случайного выбора слова из списка слов, возвращаемых API.
    return random_word["word"], random_word["subwords"]      #Оператор return возвращает слово и его подслова в виде кортежа.


load_random_word()

