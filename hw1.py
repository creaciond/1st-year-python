# variant: 4
# properties to check: a+b=c, a/b=c
a = int(input('Please type the first number: '))
b = int(input('Please type the second number: '))
c = int(input('Please type the third number: '))
if a+b == c:
    if a/b==c:
        print('a+b=c, a/b=c')
    else:
        print('a+b=c, a/b<>c')
else:
    if a/b==c:
        print('a+b<>c, a/b=c')
    else:
        print('a+b<>c, a/b<>c')