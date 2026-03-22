from datetime import date

ano_atual = date.today().year

nome = input("Qual é o seu nome?")
nascimento = int(input("Em qual ano você nasceu?"))
idade = (ano_atual - nascimento)

print(f"Olá {nome}, sua idade atualizada é {idade}")
