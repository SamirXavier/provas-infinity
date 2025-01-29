import os


arquivos = os.listdir(".")

for file in arquivos:
    print(f'{file}')