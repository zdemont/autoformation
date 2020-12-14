phrase = 'Phrase en camel case'

l = list()
for i, mot in enumerate(phrase.split(' ')):
    if i == 0:
        l.append(mot.lower())
    else:
        l.append(mot.capitalize())

print(''.join(l))

# Convertir la phrase ci-dessus dans ce format :
'phraseEnCamelCase'

