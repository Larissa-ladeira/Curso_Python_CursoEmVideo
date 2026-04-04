nomecompleto = str(input("Digite um nome completo: "))
semespaços = nomecompleto.replace(" ","")
primeironome = nomecompleto.split()[0]

print(f'Seu nome em Maiúsculo: {nomecompleto.upper()}'
      f'\nseu nome em Minúsculo: {nomecompleto.lower()}'
      f'\nAs letras do seu nome sem espaços {semespaços} contém: {len(semespaços)} caracteres'
      f'\nSeu primeiro nome {primeironome} contém : {len(primeironome)} caracteres')

