# Максимова Дарья, 153
# вариант 1

# задание 1: вывести на экран все строчки длиной боле 20 символов
def printlines():
    fv = open('newtext.txt','r',encoding='utf-8')
    for line in fv.readlines():
        if len(line) > 20:
            print(line)
    fv.close()

def gettext():              # "собрать" весь текст для задания 2
    fv = open('newtext.txt','r',encoding='utf-8')
    text = ''
    for line in fv.readlines():
        line = line.strip(' ')
        line = line.lower()
        text += line
    fv.close()
    return text

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# задание 2: код буквы - её последнее вхождение
def codes(text):
    codes = []
    for letter in alphabet:
        code = text.rfind(letter) + 1
        print(letter, code)
        codes.append(code)
    return codes

def getwords():                 # ввод слов для задания 3
    wordstoencode = []
    print('\r\nВведите слова для шифровки, чтобы закончить, введите пустое слово:')
    word = input()
    while word != '':
        wordstoencode.append(word)
        word = input()
    return wordstoencode

# задание 3: шифровка введённых слов
def encode():
    charcodes = codes(gettext())            ## список с кодом каждой буквы
    for word in getwords():
        # проверка на вшивость!
        marks = ' .,-?!—()"abcdefghijklmnopqrstuvwxyz01234567890'
        f = 1
        for mark in marks:
            if mark in word:
                print('Не только лишь алфавит')
                f = 0
        if f == 1:
            output = ''
            for sym in word:
                output += (' ' + str(charcodes[alphabet.find(sym)]))
            output = output.strip(' ')
            print(output)

def main():
    printlines()
    encode()

    
if __name__ == '__main__':
    main()
