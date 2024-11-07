produtos = {}
 
total = 0


for i in range(1,6):
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    total += preco
    produtos[nome] = preco
    print("-------------------------------")
    
print(produtos)
print(f"a soma foi: {total:.2f}")