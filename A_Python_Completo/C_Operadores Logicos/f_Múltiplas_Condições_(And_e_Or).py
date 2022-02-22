def main():
    char1 = 'a'
    char2 = 'a'

# Para ter todas as condições verdadeira usamos o AND.
    if char1 == 'F' and char2 == 'B':
        print("Felip & ByLearn")
    elif char1 == 'F':
        print("Felip")
    elif char2 == 'B':
        print("ByLearn")
    else:
        print("Python")    

main()

def main():

    numero_escolhido = 3

    primeiro_chute = 3
    segundo_chute  = 2
    terceiro_chute = 5 

# Para que pelo menos uma condição seja verdade usamos o OR
    if (primeiro_chute == numero_escolhido) or (segundo_chute == numero_escolhido) or (terceiro_chute == numero_escolhido):
        print("Você acertou em pelo menos um dos chutes")
    else:
        print("Você errou todos os chutes")

main()

def main():
    cond1 = True
    cond2 = False

    if cond1 and cond2:
        print("Todas São Verdadeiras")
    elif cond1 or cond2:
        print("Uma é Verdaira")
    else:
        print("Ambas São Falsas")
main()

def main():
    cond_obrigatoria = True
    cond_opcional1 = False 
    cond_opcional2 = True

    if cond_obrigatoria and cond_opcional1 and cond_opcional2:
        print("Todas São Verdadeiras")
    elif cond_obrigatoria and (cond_opcional1 or cond_opcional2):
        print("A obrigatoria é Verdaira e pelo menos uma das Opcionais é Verdadeira")
    elif cond_obrigatoria:
        print("A penas a obrigatoria é verdadeira")
    elif cond_opcional1 and cond_opcional2:
        print("A obrigatoria e Falsa, Mas as Opcionais são Verdadeira")
    elif cond_opcional1 or cond_opcional2:
        print("A obrigatoria e Falsa, Mas pelo menos uma das Opcionais é Verdadeira")
    else:
        print("Ambas São Falsas")
main()