# Максимова Дарья, 153, вариант 4

import os


def getletters():
    dirbegins = {}
    for root, dirs, files in os.walk('.'):
        for dirname in dirs:
            dirname = dirname.lower()
            if dirname[0] in dirbegins:
                dirbegins[dirname[0]] += 1
            else:
                dirbegins[dirname[0]] = 1
    return dirbegins


def main():
    letters = getletters()
    ## values = частотность букв, keys = сами буквы
    maxit = max(letters.values())
    letters2 = {v:k for k, v in letters.items()}
    ## а теперь наоборот
    for l in letters:
        if letters[l] == maxit:
            print(letters2[maxit])


if __name__ == '__main__':
    main()
