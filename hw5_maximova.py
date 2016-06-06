# variant: 4
# input: text file
# output: percentage of words ending with marks

marks = ['.', ',', '?', '!']
text = open('random_text.txt', 'r', encoding='utf-8')
lines = text.readlines()
word_count = 0                  # total
marked_words = 0                # words w/marks
for item in lines:
    words = item.split(' ')
    word_count += len(words)
    for i in range(len(words)):
        for j in range(len(marks)):
            if words[i].endswith(marks[j]):
                marked_words += 1
if marked_words != 0:
    print('Percentage of words with marks: ', round(marked_words/word_count*100, 1))
else:
    print('There are no words with marks.')