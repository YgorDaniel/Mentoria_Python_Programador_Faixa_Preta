# Tipos de Variável

'''
str -> String texto
int -> Número inteiro
float -> Número decimal

'''
print(type(23))
print(type("23"))

print("###############################") 
# int -> Número inteiro
def main():
    a = int(input("Digite o primeiro numero "))
    b = int(input("Digite o segundo numero "))
    soma = a + b

    print("Tipo de a:", type(a))
    print("Tipo de b:", type(b))
    print("Soma =",soma)

main() 

print("###############################") 

# float -> Número decimal
def main():
    a = float(input("Digite o primeiro numero "))
    b = float(input("Digite o segundo numero "))
    soma = a + b

    print("Tipo de a:", type(a))
    print("Tipo de b:", type(b))
    print("Soma =",soma)

main() 

#Exercicio 2.3
print("###############################") 
print("Exercicio 2.3") 
print("Fazer uma função que multiplique dois numeros entrados pelo usuário")
def main():
    a = float(input("Digite o primeiro numero "))
    b = float(input("Digite o segundo numero "))
    multiplicacao = a * b

    print(f"Multiplicação {a} * {b} = {multiplicacao}")
main()

 # Exercicio 2.4
print("###############################") 
print("Exercicio 2.4")  
print("Fazer uma função que divida dois numeros entrados pelo usuário")
def main():
    a = float(input("Digite o primeiro numero "))
    b = float(input("Digite o segundo numero "))
    divisao = a / b

    print(f"Divisão {a} / 47{b} = {divisao}")
main() 


# Exercicio 2.5
print("###############################") 
print("Exercicio 2.5")
print("Fazer uma função que subtraia quatro numeros entrados pelo usuário")
def main():
    a = float(input("Digite o primeiro numero "))
    b = float(input("Digite o segundo numero "))
    c = float(input("Digite o terceiro numero "))
    d = float(input("Digite o quarto numero "))
    subtracao = a - b - c -d

    print(f"Subtração {a}-{b}-{c}-{d} = {subtracao}")
main() 