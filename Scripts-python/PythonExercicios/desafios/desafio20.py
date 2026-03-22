# import random
"""
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do Quarto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print("-" * 20)
print("ORDEM DE APRESENTAÇÃO:")

for i, nome in enumerate(lista):
    print(f"{i + 1}º {nome}")
"""
#Resolução guanabara

from random import shuffle
n1 = (input("Primeiro aluno: "))
n2 = (input("Segundo aluno: "))
n3 = (input("Terceiro aluno: "))
n4 = (input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação sera ')
print(lista)
