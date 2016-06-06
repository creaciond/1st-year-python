# Максимова Дарья, 153
# вариант 4

import random


def getwords():
    fv = open('guessaword_maximova.csv','r',encoding='utf-8')
    words = {}
    for line in fv.readlines():
        var = line.split(',')
        words[var[0]] = var[1].strip('\r\n')               # загаданное слово(=ключ) : подсказка (=значение)
    fv.close()
    return words


def getaguess(wordsdict):                                  # выбираем слово для угадайки
    words = []
    for item in wordsdict:
        words.append(item)                                 # кидаем все ключи в один список
    choice = random.choice(words)
    return choice


def getahint(choice, wordsdict):                           # кол-во точек = кол-ву букв в подсказке-прилагательном
    hint = '.' * len(wordsdict[choice])
    return hint


def main():
    words = getwords()                              # словарь
    word = getaguess(words)                         # загаданное слово
    guess = input(words[word] + ' ' + getahint(word, words) + '\r\n')
    if guess.lower() == word:
        print('Верно!')
    else:
        print('Неверно :(')

if __name__ == '__main__':
    main()