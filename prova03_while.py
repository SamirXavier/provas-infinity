# Definir o número a ser adivinhado e o número de tentativas
num = 7
tentativas = 3


# Laço while para que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas
while tentativas > 0:
    palpite = int(input("digite um numero: "))
    if palpite == num:
        print(f"parabéns, você acertou o numero correto é: {num} ")
        break
    else:
        tentativas -= 1
        print(f"você errou! tente novamente, tentativas restantes: {tentativas}")


# Esse else é executado se o jogador não acertou após todas as tentativas
else:
    print(f"suas 3 tentativas acabaram. infelizmente nao foi dessa vez, o numero correto era: {num} ")
    
