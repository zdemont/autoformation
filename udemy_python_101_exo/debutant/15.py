lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"

l_o = [lettre for lettre in list(phrase.lower()) if lettre == 'o']

print(len(l_o))



# solution
print(phrase.lower().count(lettre_a_chercher))