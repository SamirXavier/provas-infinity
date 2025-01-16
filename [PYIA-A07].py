import random

def lancar_dados ():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    soma = (d1+d2)
    print(f"Resultados dos dados: {d1} e {d2}")
    return soma

print(f"Soma total: {lancar_dados()}")