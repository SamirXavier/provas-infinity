def media(a,b,c):
    print(f"a media aritimética é: {(a+b+c)/3}")


num_a = 0
num_b = 0
num_c = 0



for i in range(3):
    num = float(input("digite um numero: "))
    if i == 0:
        num_a = num
    elif i == 1:
        num_b = num
    elif i == 2:
        num_c = num
        
media(num_a,num_b,num_c)