## Максимова Дарья, БКЛ153
import re


## поиск по регулярному выражению в строке и добавление результатов в массив
def regexsearch(regex, text, array):
    res = re.findall(regex, text)
    if res:
        for each in res:
            array.append(each)


## 1 (5 баллов). Найти и распечатать на экране все упоминания имен
## вида "инициал + фамилия" (например: Я. Меттенлейтер).
def getInitials():
    f = open('Михайловский_замок.html', 'r', encoding='utf-8')
    regex = '[А-ЯЁ]\. [А-ЯЁ][а-яё]+'
    results = []
    for line in f.readlines():
        res = re.findall(regex,line)
        if res:
            for each in res:
                each = each.strip(' ')
                results.append(each)
    f.close()
    return results


## 2 (8 баллов). Найти в статье вообще все имена (инициалы + фамилия, например,
## В. И. Наливайко; имя + фамилия, например, Винченцо Бренна). При этом в найденное
## может попасть лишнее (например, Круглому Тронному), но не должно ничего теряться.
def getNames():
    names = getInitials()                                       # Н.Лесков
    fullregex = '[А-ЯЁ]\.[А-ЯЁ]\. [А-ЯЁ][а-яё]+'                # Н.С. Лесков
    reverseregex = '[А-ЯЁ][а-яё]+ [А-ЯЁ]\.(?:[А-ЯЁ]\.)'         # Лесков Н.С.
    nameregex = '[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+'                   # Николай Лесков
    f = open('Михайловский_замок.html', 'r', encoding='utf-8')
    for line in f.readlines():
        regexsearch(fullregex, line, names)
        regexsearch(reverseregex, line, names)
        regexsearch(nameregex, line, names)
    f.close()
    for each in names:
        print(each)
    return names


## 3 (10 баллов). Для каждого найденного в предыдущем пункте случая отделить имя
## (или инициалы) от фамилии, для каждой фамилии создать отдельную папку, а внутри
## неё для каждого сочетания "инициалы + фамилия" или "имя + фамилия" создать
## текстовый файл с предложением, в котором упоминается это вхождение.

        

def main():
    getNames()

if __name__ == '__main__':
    main()
