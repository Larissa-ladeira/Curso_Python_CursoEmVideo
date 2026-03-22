dinheiro = float(input("Digite quantos reais você tem: R$ "))
dolar = dinheiro/5.30
euros = dinheiro/6.06
iene = dinheiro * 30
print(f"Com R$ {dinheiro:.2f} reais. "
      f"\nVocê pode comprar U${dolar:.2f} dolares. "
      f"\nVocê pode comprar €{euros:.2f} euros. "
      f"\nVocê pode comprar ¥{iene:.2f} Ienes.")

# Resolção Guanbara
# real = float(input("Quanto dinheiro você tem na carteira? R$ "))
# dolar = real/5.30
# print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
