#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

name = str(input("Digite seu nome completo: ")).strip()

print("Analisando o seu nome...")
print(f'Seu nome em maiúsculo é {name.upper()}')
print(f'Seu nome em minúsculo é {name.lower()}')
print(f"Quantidade de letras é {len(name) - name.count(' ')}")
print(f"Letras no primeiro nome: {len(name.split()[0])}")