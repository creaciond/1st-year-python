# variant: 4
# input: number
# output (given input is 4):
# 4 3 2 1
# 4 3 2
# 4 3
# 4

num = int(input('Type a number: '))
for i in range(num + 1):
    line = ''
    for j in range(num - i):
        line = line + str(num - j) + ' '
    print(line)
