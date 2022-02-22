def main():
    primeira_nota = float(input("Digite a primeira nota: "))
    Segunda_nota = float(input("Digite a segunda nota: "))
    media = (primeira_nota + Segunda_nota)/2
    
    if media >= 6.0:
        print(f"Sua media é {media}, você foi aprovado")
    else:
        print(f"Sua media é {media}, você foi reprovado")
main()