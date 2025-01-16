def  maior_numero (n1,n2,n3):
    num_M = max(n1,n2,n3)
    return(num_M)

num1 = int(input("digite um numero: ")) 
num2 = int(input("digite um numero: ")) 
num3 = int(input("digite um numero: ")) 

print(f"o maior numero e: {maior_numero(num1,num2,num3)}")