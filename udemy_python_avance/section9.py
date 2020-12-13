import string


prenom = 'Astrid'

# Ma proposition 
alphabet = list(string.ascii_lowercase)
alphabet_pos = [string.ascii_lowercase.index(letter)+1 for letter in alphabet]
combinaison_alphabet = list(zip(alphabet, alphabet_pos))

match = [(p_letter, com_alph[1])  for p_letter in list(prenom) for com_alph in combinaison_alphabet  if p_letter.lower() == com_alph[0]]

for t in match:
    print(f'{t[0]} -> {t[1]}')
  
# A -> 1
# s -> 19
# t -> 20
# r -> 18
# i -> 9
# d -> 4


# LA SOLUTION
indice = [string.ascii_lowercase.index(letter)+1 for letter in prenom.lower()]
combinaison = list(zip(prenom, indice))
result = [f'{c[0]} -> {c[1]}' for c in combinaison]
result_format = '\n'.join(result)
print(result_format)