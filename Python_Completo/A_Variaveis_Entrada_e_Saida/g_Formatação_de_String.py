#Formatção de string


numero = 10
letra = "a"
palavra = "ByLearn"

'''Podeomos formatar com format'''
print("Minha letra {1}, Minha palavra é {2} , meu número vale {0}".format(numero, letra, palavra))

'''Podemos formatar com o f-String'''
print(f"Minha letra {letra}, Minha palavra é {palavra} , meu número vale {numero}")

# Formatando Numero "Arredondamento"
'''
d -> Inteiros 
f -> Float
'''

'''Com format'''
a = 10
b = 3
divisao = a / b
print(divisao)
print('{:.2f}'.format(divisao))
print('{:.1f}'.format(divisao))
print('{:.0f}'.format(divisao))

'''Com o f-String'''
a = 12
b = 7
divisao = a / b
print(divisao)
print(f'{divisao:.2f}')
print(f'{divisao:.1f}')
print(f'{divisao:.0f}')
