def concatenation_chemin(base, *args):
    return '/'.join([base]+list(args))
    
chemin_complet = concatenation_chemin('C:/Utilisateurs', 'ThibH', 'Images')
print(chemin_complet)



# solution 

import os

def concatenation_chemin(*args):
    chemin = os.path.join(*args)
    return os.path.normpath(chemin)

chemin_complet = concatenation_chemin('C:/Utilisateurs', 'ThibH', 'Images', 'France')
print(chemin_complet)