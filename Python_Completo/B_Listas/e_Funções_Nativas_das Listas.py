# Funções Nativas das Listas

def main():
    nomes_p = ['Paulo','Pascal','Patrícia','Patrick','Pamela',
               'Pedro','Péricles','Penélope','Perseu',
               'Pierre','Pilatos','Pitágoras',
               'Poliana','Pompéia']
    print(nomes_p)

    print('#############################################')
    print('Função append()=> Insere um elemento no final da lista') 
    nomes_p.append('Publia')
    print(nomes_p)

    print('#############################################')
    print('Função index()=> Retorna o indice de um determinado elemento na lista') 
    indicenome_p =nomes_p.index('Publia')
    print(indicenome_p)
    
    print('#############################################')
    print('Função in=> Checa a existência OU não existência do elemento na lista')    
    print('Paloma' in nomes_p)
    print('Publia' in nomes_p)

    
    print('#############################################')
    print('Função insert()=> Inseri um elemento na lista em uma determinada posição') 
    nomes_p.insert(0,'Paloma')
    print(nomes_p)

    print('#############################################')
    print('Função remove()=> Remove um determinado elemento da lista') 
    nomes_p.remove('Paulo')
    print(nomes_p)

    print('#############################################')
    print('Função pop()=> Remove um elemento em um determinado indice da lista')
    #pop interage com a lista, apenas removendo o elemento do indice enviado por parâmetro 
    nomes_p.pop(3)
    print(nomes_p)

    print('#############################################')
    print('Função del()=> Remove um elemento em um determinado indice da lista') 
    #del remove o elemento passado por parâmetro(envio um elemento)
    del(nomes_p[2])
    print(nomes_p)

    print('#############################################')   
    print('Função sort()=> Ordena a lista')        
    print(nomes_p)
    print('---------------------------------------------')
    nomes_p.sort()
    print(nomes_p)
    print('---------------------------------------------')
    print('Interage diretamente na lista...Não retorna nada') 
    print(nomes_p.sort())
    print('Não da para atribuir') 
    nomes_p02 =nomes_p.sort() 
    print(nomes_p02)

    print('#############################################')   
    print('Função sorted()=> Ordena a lista')
    lista_numeros01 = [3,9,7,2,5,1,4,6,8,10]
    print(lista_numeros01)
    print('Retorna uma lista ja ordenada')    
    print(sorted(lista_numeros01))

    print('Consegue atribuir')
    lista_numeros02 = sorted(lista_numeros01)      
    print(lista_numeros02)

main()