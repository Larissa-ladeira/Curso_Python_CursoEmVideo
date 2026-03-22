preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.05
precocomdesconto = preco - desconto
print(f"Você recebeu um desconto de 5% no seu produto,"
      f"\n de R$ {preco} com menos R${desconto:.2f} "
      f"\nseu produto ficou por R${precocomdesconto:.2f}")

#Resolução guanabara
# preco = float(input("Qual é o preço do produto? R$ "))
# novo = preco - (preco * 5/100)
# precocomdesconto = preco - desconto
# print("O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preco, novo))
