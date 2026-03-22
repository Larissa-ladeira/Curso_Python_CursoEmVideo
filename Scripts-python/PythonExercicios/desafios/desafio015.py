dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
totalapagar = (dias * 60) + (km * 0.15)

print(f"O total a pagar é de R${totalapagar:.2f}")

#Resolução do Guanabara
# dias = int(input("Quantos dias alugados? "))
# km = float(input("Quantos km rodados? "))
# pago = (dias * 60) + (km * 0.15)
# print("O total a pagar é de R${:.2f}".format(pago))
