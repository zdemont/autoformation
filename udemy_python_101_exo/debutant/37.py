while True:
    print("Entrez l'age du chien: ")
    age = int(input()) 
    if age < 0:
        print('Entrer un age positif')
    
    elif 0 <= age <= 2:
        print(f"L'age humain du chien est : {str(age*10.5)}")
        
    else: 
        print(f"L'age humain du chien est : {str(21+(age-2)*4)}")
