# Mostrar todos os numeros Pares
def main():
    numero = int(input("DIGITE UM NUMERO: "))
    for i in range(numero + 1):
        if i == 15:
            break
        if i % 2 == 0:            
            print(i)

main()

print("##################################")

def main():
    numero = int(input("DIGITE UM NUMERO: "))
    for i in range(numero + 1):
        if i == 15:
            break
        if i % 2 == 0:
            continue            
        print(i)

main()

print("##################################")

def main():

    i = 0
    numero = int(input("DIGITE UM NUMERO: "))
    while i <= numero:

        i+=1
        if i == 15:
            break
        if i % 2 == 0:
            print(i)

main()

print("##################################")

def main():

    i = 0
    numero = int(input("DIGITE UM NUMERO: "))
    while i <= numero:

        i+=1
        if i == 15:
            break
        if i % 2 == 0:
            continue
        print(i)

main()


print("##################################")

def main():

    i = 0
    numero = int(input("DIGITE UM NUMERO: "))
    while i <= numero:

        i+=1

        if i % 2 == 0 and i < 15 :            
            print(i)

main()



