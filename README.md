# Программирование, 1 курс

Домашки нумеруются по порядку: hwNN.py. Все домашние работы, к которым прилагаются ещё другие файлы, "расфасованы" по папкам.

## Домашнее задание 1
Вам надо написать на питоне программу, которая спрашивала бы у пользователя три числа (a, b и c), а дальше, в зависимости от номера Вашего варианта, сообщала бы пользователю, обладают или не обладают введённые числа некоторыми свойствами:
* a и b в сумме дают c
* a разделить на b равно c

## Домашнее задание 2
Спрашивает у пользователя слово и число и выводит на экран введённое слово введённое число раз.

## Домашнее задание 3
Нужно написать программу, которая спрашивает у пользователя натуральное число n и, в зависимости от варианта, печатает тот или иной набор строчек из чисел, в котором будет n строк и n столбцов такого вида:
4 3 2 1
4 3 2
4 3
4

## Домашнее задание 5 
Программа должна спрашивать у пользователя латинские слова до тех пор, пока он не введёт пустое слово. После этого программа должна вывести на экран те из введённых слов, которые с большой вероятностью являются инфинитивами (каждое слово на отдельной строчке). [Словами типа esse можно не заморачиваться, но пассивный инфинитив надо учесть.]

## Домашнее задание 6
Программа должна открывать файл с русским текстом в utf-8 и сообщать про него следующую информацию: какой процент от общего количества слов не оканчивается знаком препинания (можно взять только запятую и точку)

## Домашнее задание 7
Загадав существительное, программа показывает подсказку в виде распространённого словосочетания с этим существительным, в котором существительное заменено многоточием, и ждёт ответа пользователя, после чего сообщает, выиграл он или проиграл. Например, если загадано слово "снег", можно показать подсказку "белый ...". Словосочетание можно подсмотреть в корпусе: http://ruscorpora.ru/beta/search-ngrams_2.html или довериться интуиции.
В задании обязательно использовать словарь. Программа должна уметь загадывать как минимум 5 разных слов (с разными подсказками). Кроме того, желательно, чтобы слова и подсказки хранились в отдельном csv-файле, который загружался бы при запуске программы.
Многоточие должно содержать столько точек, сколько букв в подсказке.

**NB:** к этой домашке лежит файл ```guessaword.csv```

## Хокку
Вам нужно написать программу, порождающую случайные грамматически правильные, но бессмысленные тексты. Слова для текстов должны быть взяты из отдельных txt-файлов, открываемых программой. Эти файлы следует прислать вместе с кодом выполненного домашнего задания. При написании кода старайтесь активнее использовать возможность создания функций, желательно в функции уложить вообще весь код.
Текст должен представлять собой правильное хайку, то есть стихотворение на одном из изучаемых вами языков (французский, немецкий, итальянский?) из трёх строк без рифмы, при этом длина первой строки должна быть 5 слогов, второй строки - 7 слогов, третьей строки - 5 слогов. Количество предложений в таком тексте может быть любым.
Хокку состоит из:
* ```hokku.py```,
* ```noms_m.txt```, ```noms_f.txt```,
* ```adjectifs.txt```,
* ```verbes.txt```

## Домашнее задание 8
Программа должна открывать файл с русским текстом в кодировке UTF-8 и распечатывать из него по одному разу все встретившиеся в нём формы глагола "выпить"

**NB:** этой домашки нет.

## Домашнее задание 9
В некоторых статьях Википедии на какую-то определённую тему есть стандартные шаблоны-карточки, в которых в кратком виде изложена основная информация. Например, для людей это дата рождения и смерти, для стран -- столица, население и т. п. Поскольку карточки устроены стандартным образом, с таких страниц можно автоматически собирать информацию. Этим и должна заниматься Ваша программа из очередного дз. Она должна открывать заранее сохранённый html-файл со статьёй из русской википедии на определённую тему с определённой карточкой и доставать оттуда кое-какую информацию. Полученную информацию она должна записать в текстовый файл.

*Тема:* статьи об учёных (напр., Эйнштейн, Альберт)

*Информация:* научная сфера.

**NB:** к этой домашке лежит файл ```wiki.htm```

## Домашнее задание 10

### Про дореформенную орфографию

Если вам не хватает знаний об устройстве дореформенной орфографии, то почитать о ней можно в сочинении Я. Грота "Русское правописание" (например, [тут](http://imwerden.de/pdf/grot_russkoe_pravopisanie_1894.pdf) или [тут]( https://docs.google.com/file/d/0BwmZ0X8TCLyaM2p6VVRNV0FmTE0/edit)).

### Задание
Используя свои знания об этой системе письма и функцию ```re.findall()```, вам нужно написать программу, которая находила бы в тексте все вхождения конструкции *предложное сочетание "к + дательный падеж 2 скл." (например, "к дубу")* и записывала их в текстовый файл (каждое вхождение конструкции - на отдельной строке).

## Домашнее задание 11
Вам нужно сохранить у себя на компьютере в текстовом виде статью из Википедии "Философия". (Т. е. не HTML нужно сохранить, а только текст, например, так: открываете статью в браузере, выделяете весь текст, копируете и вставляете в заготовленный текстовый файл.) Текстовый файл, естественно, должен быть в UTF-8. Программа должна читать этот файл и заменять в нём все формы слова "философия" на соответствующие формы слова "астрология". То, что получится, она должна записывать в другой текстовый файл.

Заменяться должны только формы этого слова. Т. е. если Вам нужно заменить слово "кит" на слово "кот", слово "китовый" на слово "котовый" заменяться не должно. При замене нужно пользоваться функцией ```re.sub```. Если слово было написано с большой буквы, то и после замены оно должно быть написано с большой буквы.

## Домашнее задание 12
Программа должна обходить всё дерево папок, начинающееся с той папки, где она находится, и сообщать следующую информацию: на какую букву начинается название большинства папок (если таких много, можно печатать только одну).
