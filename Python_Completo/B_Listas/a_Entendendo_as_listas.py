#Lista

def main():
    #Criar Lista
    lista_alunos = ['Felipe', 'Alisson', 'Haynes', 'ByLearner']
    
    print(lista_alunos)
    print(f'O nome do aluno é: {lista_alunos[0]}')
    print(f'O nome do aluno é: {lista_alunos[1]}')
    print(f'O nome do aluno é: {lista_alunos[2]}')
    print(f'O nome do aluno é: {lista_alunos[3]}')
    print(f'-'*47)      
   
    #Alterar Lista
    lista_alunos[2] = 'Guilherme'

    print(lista_alunos)
    print(f'O nome do aluno é: {lista_alunos[0]}')
    print(f'O nome do aluno é: {lista_alunos[1]}')
    print(f'O nome do aluno é: {lista_alunos[2]}')
    print(f'O nome do aluno é: {lista_alunos[3]}')
    print(f'-'*61)

    #Acresentar dados a lista
    lista_alunos.append('Novo Aluno')
        
    print(lista_alunos)    
main()
    