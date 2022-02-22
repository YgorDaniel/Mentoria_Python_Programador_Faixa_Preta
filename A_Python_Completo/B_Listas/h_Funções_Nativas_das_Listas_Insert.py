# Funções Nativas das Listas

def main():
    nomes_p = ['Paulo','Pascal','Patrícia','Patrick','Pamela',
               'Pedro','Péricles','Penélope','Perseu',
               'Pierre','Pilatos','Pitágoras',
               'Poliana','Pompéia']
    print(nomes_p)       

    print('#############################################')
    print('Função insert()=> Inseri um elemento na lista em uma determinada posição') 
    nomes_p.insert(0,'Paloma')
    print(nomes_p)

main()