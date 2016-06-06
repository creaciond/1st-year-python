# coding = utf-8
# вариант 4
import re

def getfield():
    f = open('wiki.htm','r',encoding='utf-8')
    for line in f.read():
        regex = 'Научная сфера:</th>\n(.*)?\n(.*)?title="(.*)"'
        res = re.search(regex, line)
        if res:
            print(res.group(3))
        else:
            print('У Яндекса, может, найдётся всё, а здесь — нет. Попробуйте ещё раз')
    f.close()

def main():
    getfield()

if __name__ == '__main__':
    main()