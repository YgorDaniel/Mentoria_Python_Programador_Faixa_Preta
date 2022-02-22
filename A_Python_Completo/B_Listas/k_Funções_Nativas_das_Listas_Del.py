# Funções Nativas das Listas

def main():
    nomes_p = ['Paulo','Pascal','Patrícia','Patrick','Pamela',
               'Pedro','Péricles','Penélope','Perseu',
               'Pierre','Pilatos','Pitágoras',
               'Poliana','Pompéia']
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

    
main()