contador = 0

#while contador < 5:
 #   contador += 1
for i in range (5):
    print(f"---- Tentativa {i + 1} de 5 ----")
    caractere = input('Digite algo: ')
    if caractere.isnumeric():
        print(f"{caractere} é um numero ")
    elif caractere.isalpha():
        print(f"{caractere} é uma string ")

    elif caractere.isalnum():
        print(f"{caractere} é alfanumerico")
    else:
        print(f"{caractere} é um caractere especial")
'''
#Guanabara resolução + laço de repetição que eu coloquei para testar

for i in range (5):
    print(f"---- Tentativa {i + 1} de 5 ----")

    a = input('Digite algo:')
    print("O tipo primitivo desse valor é", type(a))
    print("Só tem espaços?", a.isspace())
    print("É um número?", a.isnumeric())
    print("É alfabético?", a.isalpha())
    print("É alfanumerico?", a.isalnum())
    print("Está em maiusculas?", a.isupper())
    print("Está em minusculas?", a.islower())
    print("Está capitalizada?", a.istitle())
'''
