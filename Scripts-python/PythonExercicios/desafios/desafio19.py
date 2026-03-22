
import random

nome1 = input("primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")
lista = ([nome1, nome2, nome3, nome4])
print(f'O aluno escolhido foi {random.choice(lista)}')


#Resolução guanabara
# from random import choice
#
# n1 = int(input("Primeiro aluno: "))
# n2 = int(input("Segundo aluno: "))
# n3 = int(input("Terceiro aluno: "))
# n4 = int(input("Quarto aluno: "))
# lista = ([n1, n2, n3, n4])
# escolhido = choice(lista)
# print(f'O aluno escolhido foi {}'.format(escolhido))
