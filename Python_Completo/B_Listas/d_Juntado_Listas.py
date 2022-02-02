# Juntado_Listas(join)

def main():

    numerospares = [2,4,6,8,10]
    numerosimpares = [1,3,5,7,9]
    numerosromanos = ['I','II','III','IV','V','VI','VII','VIII','IX','X']

    print('Exemplo01 - juntar listas')    
    juntar_listas = numerospares + numerosimpares + numerosromanos
    print(juntar_listas)

    print('########################################################')
    print('Exemplo02 - juntar listas')   
    juntar_listas = numerospares + numerosimpares
    print(juntar_listas)
    
    juntar_listas += numerosromanos
    print(juntar_listas)
main()