# Funções Nativas das Listas

def main():
    nomes_p = ['Paulo','Pascal','Patrícia','Patrick','Pamela',
               'Pedro','Péricles','Penélope','Perseu',
               'Pierre','Pilatos','Pitágoras',
               'Poliana','Pompéia']
    print(nomes_p)  

    print('#############################################')   
    print('Função sort()=> Ordena a lista')        
   # print(nomes_p)
   # print('---------------------------------------------')
    nomes_p.sort()
    print(nomes_p)
    print('---------------------------------------------')
    print('Interage diretamente na lista...Não retorna nada') 
    print(nomes_p.sort())
    print('Não da para atribuir') 
    nomes_p02 =nomes_p.sort() 
    print(nomes_p02)

main()