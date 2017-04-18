# Максимова Дарья, 153, вариант 4

import re

def main():
    f = open('rur.txt', 'r', encoding='utf-8')
    for line in f.readlines():
        res = re.findall(" ((?:К|к)ъ [а-яёѣ]*?[уиѣ])[ .,?!]", line)
        for item in res:
            print(item)
    f.close()

if __name__ == '__main__':
    main()