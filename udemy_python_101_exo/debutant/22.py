# 1. get prenom 
# 2. get p

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}

# 1.
prenom = employes.get('01',).get("identite").get('prenom')

# 2.
prenom = employes.get('01', {}).get("identite", {}).get('prenom', {})

print(prenom)


# Solution
prenom = employes.get('01', {}).get("identite", {}).get('prenom', "valeur inconnue")
