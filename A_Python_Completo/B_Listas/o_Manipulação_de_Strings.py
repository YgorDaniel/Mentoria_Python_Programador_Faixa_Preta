def main():
    # Caratere é uma Letra só
    char = 'c'
    # String é conjuto de caracteres
    # Vetor (Array)=> Sequencia de elementos do mesmo tipo
    # String é um Vetor (Array) de caracteres
    string = "ByLearn"
    print(string[0])
    print(string[1])
    print(string[2])
    print(string[3])
    print(string[4])
    print(string[5])
    print(string[6])

    #String Podem ser fatiadas, como por exemplo, para madar o valor de algum indice
    palavra = "teste"
    nova_palavra = palavra[:2] + 'Z' + palavra[3:]
    print(nova_palavra)
    print(palavra[-1])

    #Pesquisar em Strings 
    a = 'b' in "abc"
    b = 'd' in "abc"
    c = 'b' not in "abc"
    d = 'd' not in "abc"
    print(a)
    print(b)
    print(c)
    print(d)

    # Concatenar Strings (Somar)
    string = "Fe" + "Li" + "Pe"
    print(string)

    #Alterar Para Minúsculo 
    string = "Fe" + "Li".lower() + "Pe".lower()
    print(string)

    #Alterar Para Maiúsculo
    string = "Felipe".upper() 
    print(string)

    # Tamanho da string
    string = "Teste"
    print(len(string))

    # Checar se todos os caracteres são letras
    a = "abc".isalpha()
    b = "1bc".isalpha()
    c = "123".isalpha()
    d = "++ ; / ".isalpha()
    print(a)
    print(b)
    print(c)
    print(d)

    # Remover espaços em branco tanto no inicio quanto no final
    a = "          Sobrando Espaços    "
    print(a)

    print(a.strip())

    #Juntar os itens da String através de um delimitador
    a = "abc"
    print(a)

    print(",  ".join(a))
    
    # Separar uma string através de um delimitador
    string = "N#o#m#e"
    print(string)

    print(string.split("#"))

main()    