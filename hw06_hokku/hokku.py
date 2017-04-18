# Максимова Дарья, БКЛ153, вариант 4

# coding: utf-8
import random

# получаем _одно_ случайное слово из файла, который в аргументе функции
def getword(filename):
    wchoice = ''
    filename += '.txt'
    wfile = open(filename, 'r')
    words = wfile.read().split('\n')
    wfile.close()
    wchoice = random.choice(words)
    return wchoice


# подсчёт слогов: (все гласные [минус дифтонги] [минус е немое])
def sylcount(word):
    words = word.split(' ')
    sc = 0
    vowels = 'aeiouyéèàùëïüÿâêîôû'
    diftongs = ['ai', 'eau', 'ei', 'eu', 'oeu', 'oi', 'ou']
    for thisword in words:
        for sym in thisword:
            if sym in vowels:
                sc += 1
        for dif in diftongs:
            if dif in thisword:
                sc -= (len(dif) - 1)                                      # дифтонг = 1 гласный звук
                if dif == 'oeu':                                          # если это oeu, то его мы посчитали дважды
                    sc += 1
        if thisword.endswith('e'):                                        # е немое
            sc -= 1
    return sc


# сделать прилагательное женского рода
def femadj(adj):
    if adj.endswith('el') or adj.endswith('en') or adj.endswith('ien') or adj.endswith('on'):
        adj = adj + adj[-1] + 'e'                                       # удвоить последнюю букву + e
    elif adj.endswith('f'):
        adj = adj[0:len(adj) - 2] + 've'                                # f -> ve
    elif adj.endswith('eux'):
        adj = adj[0:len(adj) - 2] + 'se'                                # eux -> euse
    elif adj.endswith('e'):
        return adj                                                      # triste -> triste
    else:
        adj += 'e'
    return adj


# прилагательное
def get_adj(genre):
    adj = ''
    if round(random.random()) == 0:
        adj = ''
    else:
        adj = ' ' + getword('adjectifs')
        if genre == 'f':
            adj = femadj(adj)
    return adj


# la aide -> l'aide
# будет время — избавься от брейка, а то чёт ниоч
# (подсказка: логические переменные или что-то типа)
def contrac(word1, word2):
    contr = ''
    vowen = 'aeiouy'                                                # окончание 1 слова
    vowst = 'haeiouyéèàùëïüÿâêîôû'                                  # начало 2 слова
    if word1[-1] in vowen:
        if word2[0] in vowst:
            contr = word1[0:(len(word1) - 1)] + '\'' + word2
        else:
            contr = word1 + ' ' + word2
    return contr


# именная группа (сущ + прил)
def get_NP():
    if round(random.random()) == 0:
        NP = contrac('le', getword('noms_m'))
        NP += get_adj('m')
    else:
        NP = contrac('la', getword('noms_f'))
        NP += get_adj('f')
    return NP


# глагол (+ согласование 3л)
def get_VP():
    verb = getword('verbes')
    if verb.endswith('er'):
        verb = verb[0:(len(verb) - 2)] + 'e'
    elif verb.endswith('ir'):
        verb = verb[0:(len(verb) - 1)] + 't'
    return ' ' + verb

# подбор: по идее, надо бы избавиться от рекурсии, а то чёт ниоч [2]
# подбор существительного-дополнения, чтобы "забить" строку
def fillobj(sgoal):
    obj = get_NP()
    if sylcount(obj) == sgoal:
        obj = ' ' + obj
    else:
        fillobj(sgoal)
    return obj


# подбор глагола, чтобы влезть в лимит по слогам
def fillverb(sgoal):
    verb = get_VP()
    if sylcount(verb) == sgoal:
        verb = ' ' + verb
    else:
        fillverb(sgoal)
    return verb


# собираем строку, учитывая лимит по слогам
def makeline(sylnum):
    # сначала subject
    line = get_NP().capitalize()
    if sylcount(line) == sylnum:
        return line + '.'
    elif sylcount(line) < sylnum:
        # если место ещё есть, добавляем глагол
        line += get_VP()
        if sylcount(line) == sylnum:
            return line + '.'
        elif sylcount(line) < sylnum:
            # если место снова есть, то ищем такую NP, которая влезет
            line += (fillobj(sylnum - sylcount(line)))
        else:
            # если нынешний глагол не влез, то ищем такой, какой влезет
            line += (fillverb(sylnum - sylcount(line)))
    return line + '.'


def make_a_hokku():
    hokku = makeline(5) + '\r\n' + makeline(7) + '\r\n' + makeline(5)
    return hokku


if __name__ == "__main__":
    print(make_a_hokku())