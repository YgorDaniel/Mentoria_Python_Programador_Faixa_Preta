def main():
    import random

    print("Jogo do numero mágico digite um numero que o mágico tenta adivinhar")
    numeroescolhido = int(input("Digite um numero 1 a 5: "))
    numeromagico = random.randint(1,5)
    
    if numeromagico == numeroescolhido:
        print(f"Mágico: O numero é {numeromagico}\nVocê: Acertou")
    elif numeromagico > numeroescolhido:
        print(f"Mágico: O numero é {numeromagico}\nVocê: Diminua o Chute")
    else :
        print(f"Mágico: O numero é {numeromagico}\nVocê: Aumente o Chute")

main()