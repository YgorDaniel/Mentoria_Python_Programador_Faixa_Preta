# Funções Nativas das Listas

def main():
    nomes_p = ['Paulo','Pascal','Patrícia','Patrick','Pamela',
               'Pedro','Péricles','Penélope','Perseu',
               'Pierre','Pilatos','Pitágoras',
               'Poliana','Pompéia']
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

main()