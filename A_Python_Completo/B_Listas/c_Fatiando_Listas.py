# Fatiando_Listas

def main():
    print('Referenciando uma lista para outra')
    lista_a = [1,2,3]
    lista_b = lista_a
    lista_b.append(4)

    print(lista_a)

    print(lista_b)

    print('#################################################################')
    print('Copiando os elementos de uma lista para outra')
    lista_a = [0,1,2,3,5,6,7,8,9,10]
    lista_b = lista_a [:] # Copia todos os elementos de uma lista para outra
    lista_b.append(4)

    print(lista_a)

    print(lista_b)

    print('#################################################################')
    print('Copiando os elementos entre parâmtros')
    lista_a = [0,1,2,3,4,5,6,7,8,9,10]
    lista_b = lista_a [1:4] # Copia os elementos entre 1 e 4
    

    print(lista_a)

    print(lista_b)

    print('#################################################################')
    print('Copiando os elementos até determinado parâmtro')
    lista_a = [0,1,2,3,4,5,6,7,8,9,10]
    lista_b = lista_a [:4] # Copia os elementos até 4
    

    print(lista_a)

    print(lista_b)

    print('#################################################################')
    print('Copiando os elementos a partir determinado parâmtro')
    lista_a = [0,1,2,3,4,5,6,7,8,9,10]
    lista_b = lista_a [2:] # Copia os elementos a partir 2
    

    print(lista_a)

    print(lista_b)
 
main()