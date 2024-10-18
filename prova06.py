user = "admin"
password = "1234"
tentativas = 3
while tentativas > 0:
    usuario = input("digite o nome de usuario: ")
    senha = input("digite a senha: ")
    if usuario == user and senha == password:
        print(f"bem vindo ao sistema {usuario}")
        break
    else:
        tentativas -= 1
        print(f"tentativas restantes: {tentativas}")
        
if tentativas == 0:
    for i in range(4):
        print("sistema bloqueado")



