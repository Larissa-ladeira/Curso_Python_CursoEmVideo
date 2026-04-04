numero = (input("Digite um número de 0  a 9999: ")).zfill(4)
U = numero[3]
D = numero[2]
C = numero[1]
M = numero[0]

print(f"Unidade: {U}")
print(f"Dezenas: {D}")
print(f"Centenas: {C}")
print(f"Milhar: {M}")
