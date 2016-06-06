# Максимова Дарья, БКЛ153, вариант 1
import re


# задание 1
def linecount():
    fc = open('corpus.xml', 'r', encoding='utf-8')
    fw = open('results.txt', 'w', encoding='utf-8')
    count = 0
    for line in fc.readlines():
        count += 1
    fc.close()
    fw.write('1) Строк в файле с корпусом: ' + str(count) + '\n')
    fw.close()


## вспомогательная функция, вытаскивающая строчки из файла
def getlines(filename):
    fc = open(filename, 'r', encoding='utf-8')
    lines = []
    for line in fc.readlines():
        line = line.strip(' \n')
        lines.append(line)
    fc.close()
    return lines


# задание 2
def getdict():
    dict = {}
    lines = getlines('corpus.xml')
    fw = open('results.txt', 'a', encoding='utf-8')
    for line in lines:
        if '<w lemma=' in line:
            if line in dict:
                dict[line] += 1
            else:
                dict[line] = 1
    fw.write('\n2)')                          # чтобы не сливалось
    for each in dict.keys():
        fw.write(each + '\n')
    fw.close()

        
# задание 3
def findpronouns():
    regex = 'type=\"f.h(?:.)*?\">(.*)?<'
    lines = getlines('corpus.xml')
    prlist = []
    for line in lines:
        res = re.search(regex,line)
        if res:
            prlist.append(res.group(1))
    fw = open('results.txt', 'a', encoding='utf-8')
    fw.write('\n3) Местоимения среднего рода: ' + ', '.join(prlist))
    fw.close()


def main():
    linecount()
    getdict()
    findpronouns()


if __name__ == '__main__':
    main()
