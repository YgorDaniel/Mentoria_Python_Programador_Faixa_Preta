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
    '''
    Imagina uma fila de lanches do BK
    pedidos = [1204, 1205, 1206] 
    Aí o pedido 1205 ficou pronto primeiro, pois foi bem rapidinho de fazer
    pedido_pronto = pedidos.pop(1)
    Como o pop retornou valor, você pode passar esse valor pra uma variável (pedido_pronto) 
    Em seguida entregar ao cliente
    entregar_ao_cliente(pedido_pronto)
    pedidos => [1204, 1206]
    '''
    nomes_p.pop(3)
    print(nomes_p)

    print('#############################################')
    print('Função del()=> Remove um elemento em um determinado indice da lista') 
    #del remove o elemento passado por parâmetro(envio um elemento)
    ''' 
    Imagina tem um dado inválido na lista:
    errado = [1,2, 'a', 3]
    errado.del(2)
    errado => [1,2,3]
    '''
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

    print('#############################################')   
    print('Função Len()=> Retorna o tamanho da listas')
    lista = [1, 2, 3, 4, 5, 'a', 'b', 'c']
    print(len(lista))

main()