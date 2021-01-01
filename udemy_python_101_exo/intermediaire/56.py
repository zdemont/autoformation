texte = "Bonjour Udemy"

print('-'*13)
for letter in texte:
    print('|'+' '*5+letter+' '*5+'|')
print('-'*13)

# solution 
longueur = len(texte)
 
symbole1 = "-"
symbole2 = "|"
 
print(symbole1*longueur)
 
for lettre in texte:
    print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))
 
print(symbole1*longueur)