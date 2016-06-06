# variant 4
# input: a word and a number (N)
# output: a word printed N times
string = input('Type a word and a number: ')
word = ''
num = ''
was_space = 0
for sym in string:
    if was_space == 0 and sym != ' ':
        word += sym
    elif was_space == 0 and sym == ' ':
        was_space = 1
    elif was_space == 1:
        num += sym
i = 1
while i <= int(num):
    print(i, word)
    i += 1
