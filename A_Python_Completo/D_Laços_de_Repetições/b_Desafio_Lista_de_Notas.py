def main():

    notas = []
    # Com a função range() nós podemos fazer o bloco iterar quantas vezes definirmos
    for indici in range(4,11):
        notas.append(indici)
        
    for nota in notas:
            print(nota)
main()

print("##" * 30) 

def main():

   notas = ['A', 'B', 'C', 'D', 'E', 'F']   
   for indici in range(4,11):
       notas.append(indici)
        
   for nota in notas:
            print(nota) 

main()

print("##" * 30) 

def main():

   notas = ['A', 'B', 'C', 'D', 'E', 'F']   
   for indici in range(4,11):
       notas.append(indici)
        
   for nota in range(4,11):
            print(notas[nota]) 

main()