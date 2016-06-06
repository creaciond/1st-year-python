import re


def main():
    fo = open('hw11_philosophy.txt', 'r', encoding = 'utf-8')
    fw = open('hw11_astrology.txt', 'w', encoding = 'utf-8')
    for line in fo.readlines():
        repl = re.sub('философи([а-я](?:[а-я])?)','астрологи\g<1>',line)
        repl = re.sub('Философи([а-я](?:[а-я])?)','Астрологи\g<1>',repl)
        fw.write(repl)
    fo.close()
    fw.close()


if __name__ == '__main__':
    main()
