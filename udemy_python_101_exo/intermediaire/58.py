from datetime import datetime

age = 25
mois_de_naissance = 10

today = datetime.today()

if mois_de_naissance <= today.month:
    print('case 1')
    born_year = today.year - age
else:
    print('case 2')
    born_year =  today.year - age - 1

# one line version
born_year = today.year - age if mois_de_naissance <= today.month else today.year - age - 1 
print(born_year)

# solution 
annee_actuelle = datetime.today().year
mois_actuel = datetime.today().month
 
resultat = annee_actuelle - age - (1 if mois_de_naissance > mois_actuel else 0)
print(resultat)