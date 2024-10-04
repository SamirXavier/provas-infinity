## solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo
inicio = int(input("digite um numero inteiro para inicio do intervalo: "))
fim = int(input("digite um numero inteiro para o fim do intervalo: "))
fim += 1
soma = 0
## um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares.
for i in range(inicio,fim):
    if i % 2 == 0:
        print(i)
        soma += i
        
        
## Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso, Ao final, exiba a soma dos números pares encontrados.
if soma == 0:
    print("nao há numeros pares no intervalo.")
else:
    print(f"a soma dos numeros pares do intervalo é: {soma}")