import re

# Pour chaque question, indiquez si le match est valide ou non et ce qu'il retourne.

re.match(r'[a-z]+\d{2}', 'item01')
#  match valide 
#  une chaine de caractère composer de lettre et de 2 digits

re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')
#  match valide 
#  le prenom et le nom de famille comprennant les majuscules et l'espace

re.match(r'\s+', 'pierre dupont')
# match invalide
# censé retourne des espaces blancs 


re.match(r'\w+', 'pierre dupont')
# match valide 
# retourne le nom et le prenom en deux groupe distinct


re.match(r'\w+([-+=]?)', 'pierre-dupont')
# match valide 
# retourne le nom et le prenom avec les signes -+=


re.match(r'\w+([-+=]?)', 'pierre/dupont')
# match valide
# retourne le nom et le prenom


re.match(r'\w+([-+=]+)', 'pierre/dupont')
# match invalide
# censé retourner le prenom jusqu'au signe /



# Solution 

re.match(r'[a-z]+\d{2}', 'item01')

# Match valide : retourne 'item01'

re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')

# Match valide : retourne 'Pierre Dupont'

re.match(r'\s+', 'pierre dupont')

# Match invalide : on cherche un espace au début de la chaîne de caractère, mais elle commence par une lettre.

re.match(r'\w+', 'pierre dupont')

# Match valide : retourne 'pierre'

re.match(r'\w+([-+=]?)', 'pierre-dupont')

# Match valide : retourne 'pierre-'

re.match(r'\w+([-+=]?)', 'pierre/dupont')

# Match valide : retourne 'pierre'

re.match(r'\w+([-+=]+)', 'pierre/dupont')

# Match invalide : le + cherche si les caractères -, + ou = sont présents au moins une fois ou plus dans la chaîne de caractère. Aucun de ses éléments ne se retrouve dans la chaîne de caractère au moins une fois et donc le match n'est pas valide.