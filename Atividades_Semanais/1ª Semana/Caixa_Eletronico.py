
Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de R$ 2,00 | R$ 5,00 | R$ 10,00 | R$ 20,00 | R$ 50,00 | R$ 100,00 reais.
O val'or mínimo é de R$ 2,00 reais e o máximo de R$ 1000,00 reais.

	Exemplo 1: Para sacar a quantia de R$ 256,00 reais, o programa fornece duas
	notas de R$ 100,00 uma nota de R$ 50,00  e três nota de R$ 2,00;

	Exemplo 2: Para sacar a quantia de R$ 399,00 reais, o programa fornece
	três notas de R$ 100,00 uma nota de R$ 50,00 duas notas de 20,
	uma nota de R$ 5,00 e duas notas de R$ 2,00.
'''
def main():
    
    print("A menor cédula disponivel neste terminal é R$ 2,00")
    print("Valor maximo para saque neste terminal é R$ 1000,00")

    saque = int(input("Digite o valor do saque: "))

    if 2 <= saque <= 1000:
        notas_cem = saque // 100
        saque = saque % 100

        notas_cinquenta = saque // 50
        saque = saque % 50

        notas_vinte = saque // 20
        saque = saque % 20

        notas_dez = saque // 10
        saque = saque % 10

        notas_cinco = 0
        if (saque - 5) % 2 == 0:
            notas_cinco = saque // 5
            saque = saque % 5

        if saque % 2 == 0:
            notas_dois = saque // 2
    
            if notas_cem > 0:
                print(notas_cem, "notas de R$ 100,00")
            if notas_cinquenta > 0:
                print(notas_cinquenta, "notas de R$ 50,00")
            if notas_vinte > 0:
                print(notas_vinte, "notas de R$ 20,00")
            if notas_dez > 0:
                print(notas_dez, "notas de R$ 10,00")
            if notas_cinco > 0:
                print(notas_cinco, "notas de R$ 5,00")
            if notas_dois> 0:
                print(notas_dois, "notas de R$ 2,00")

        else:
            print(f"Não é possivel sacar o valor R$ {saque}") 
                
    else:
        print("Valor permitido para saque neste terminal é de R$ 2,00 a R$ 1000,00")
    
main()
