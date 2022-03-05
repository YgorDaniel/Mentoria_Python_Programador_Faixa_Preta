def main():
    alunos = ["Felipe", "Alisson", "Haynes", "Bylearner"]
    notas = [[8,10], [10,7], [8,9], [10,10]]
     
    for aluno in alunos:
        print(f"Aluno: {aluno}")     
       
    for lista_notas in notas:
              
        soma = 0
        for nota in lista_notas:
            soma += nota   
        media = soma / len(lista_notas)       
        print(f"Media: {media}")        

main()
print('##############################################################################')
# Os laços for são muito úteis para se trabalhar com índices
def main():
    alunos = ["Felipe", "Alisson", "Haynes", "Bylearner"]
    notas = [[8,10], [10,7], [8,9], [3,5]]

    if (len(alunos) == len(notas)):
        for indice_alunos in range(len(alunos)):
            soma = 0
            for nota in notas[indice_alunos]:
                soma += nota
            media = soma / len(notas[indice_alunos])
            #print(f"Aluno: {alunos[indice_alunos]}")
            #print(f"Notas: {notas[indice_alunos]}")
            #print(f"Média: {media}")
            if media>= 6:
                    print(f"O aluno: {alunos[indice_alunos]}, Tirou as notas: {notas[indice_alunos]}, e obteve: média: {media} é foi aprovado")
            else:
                    print(f"O aluno: {alunos[indice_alunos]}, Tirou as notas: {notas[indice_alunos]}, e obteve: média: {media} é foi reprovado")                   
    else:        

        print("Tem algo de errado! \nPossivelmente algum aluno não fez Prova")
main()