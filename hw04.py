# variant 4

# input: Latin words until empty line
# output: infinitives, incl. passive

# Latin infinitives generally end in: -re (pres.act.), -ri (pres.pas.), -isse (past act.),
# -um iri (fut.pas.), -us/a/um esse (past pas., fut.act.)

word = ' '                                                  # to start the 'while' loop
possible_ends = ['re', 'ri', 'isse', 'um iri', 'us esse', 'a esse', 'um esse']
infinitives = []                                            # empty list for infinitives we'll find (if any)
print('Hit Enter when you\'re done!')
while word != '':
    word = input('Type a Latin word: ')
    for end in possible_ends:
        if word.endswith(end):
            infinitives.append(word)
if infinitives != []:
    print_line = ' '.join(infinitives)
    print(print_line)
else:
    print('Seems like you didn\'t enter any Latin infinitives. :(')
