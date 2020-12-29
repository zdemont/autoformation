import string
alphabet = string.ascii_lowercase

# for method
alphabet_dict = {}

for index, letter in enumerate(alphabet, start=1):
    alphabet_dict[index] = letter

# one line
alphabet_dict = {index:letter for index, letter in enumerate(alphabet, start=1)}

print(alphabet_dict)


# solution
indices = range(1, len(alphabet) + 1)
liste_zip = zip(indices, alphabet)
resultat = dict(liste_zip)
 
print(resultat)