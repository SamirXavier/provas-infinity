#solicitar numero de alunos
num_alunos = int(input("digite a quantidade de alunos:  "))

#declarar variaveis
soma_medias = 0
soma_notas = 0


#laço for para solicitar o nome de cada aluno
for i in range(num_alunos):
    nome = input(f"digite o nome do aluno {i+1}: ")
#zerar a variavel soma_notas para as proximas medias
    soma_notas = 0
    
#laço for para pedir as notas
    for j in range (1,4):
        nota = float(input(f"digite a nota {j}: "))
        if j == 1:
            nota_1 = nota
        elif j == 2:
            nota_2 = nota
        else:
            nota_3 = nota
        soma_notas += nota

# calcular media
    media =(soma_notas/3)

#estrutura condicional para dizer se foi "aprovado" ou "reprovado"
    if media >= 7:
        status = 'aprovado'
    else:
        status = 'reprovado'

#Exibir nome, notas, média, e status (Aprovado/Reprovado)
    print(f"nome: {nome}, nota1: {nota_1:.2f}, nota2: {nota_2:.2f}, nota3: {nota_3:.2f}, media: {media:.2f}, status: {status}. ")

# Acumular média na soma_médias  
    soma_medias += media
    

    
#calcular media geral
media_geral = soma_medias / num_alunos

#exibir a media geral da turma:
print(f"a media geral da turma foi: {media_geral:.2f}")
