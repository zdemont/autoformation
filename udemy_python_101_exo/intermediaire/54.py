# Longueur maximale à afficher
n = 8
symbole = '*'

increment = [symbole*i for i in range(1,n)]
decrement = increment[::-1]
increment.append(symbole*n)
l = increment + decrement

printer = '\n'.join(l)
print(printer)



#  solution 
nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))
for i in nombres:
    print(symbole*i)