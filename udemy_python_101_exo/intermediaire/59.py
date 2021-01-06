# somme entre deux nombres 
# script doit fonctionner peut importe le nombre

def somme(a, b):
    numbers = sorted([a, b])
    list_of_numbers = list(range(numbers[0], numbers[1]+1))
    
    return sum(list_of_numbers)

print(somme(6, 2))

# solution
def somme(a, b):
    return sum(range(min(a, b), max(a, b) + 1))