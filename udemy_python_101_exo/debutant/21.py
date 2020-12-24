

liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
liste_copy = liste[:]
# Trier la liste ici

liste.sort(key=lambda tup: tup[1])

print(liste)

# method 2 
print(sorted(liste_copy, key=lambda tup: tup[1]))

