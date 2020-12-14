import os

"""En fonction de la valeur de la variable
âge, récupérer grâce à un operateur ternaire
si la personne est majeure ou non dans la variable
'majeur'.
Si la personne est majeur, la variable
contiendra la chaîne de caractère 'majeur'.
Si la personne est mineur, la variable
contiendra la chaîne de caractère 'mineur'"""
age = 17
majeur = 'majeur' if age >= 18 else 'mineur'
print(majeur)


"""Récupérer dans la variable extension le mot 'python'
si le fichier déclaré dans la variable 'fichier' est de
type Python (extension .py). Si le fichier n'est pas
de type Python, retourner la chaîne de caractère 'invalide'"""
fichier = 'C:/Python/mon_script.py'
extension = 'python' if os.path.splitext(fichier)[1] == '.py' else 'invalide'
print('Le fichier {} est de type {}'.format(fichier, extension))


# SOLUTION 
age = 17
majeur = 'majeur' if age >= 18 else 'mineur'


fichier = 'C:/Python/mon_script.py'
extension = 'Python' if fichier.endswith('.py') else 'invalide'
print('Le fichier {} est de type {}'.format(fichier, extension))
