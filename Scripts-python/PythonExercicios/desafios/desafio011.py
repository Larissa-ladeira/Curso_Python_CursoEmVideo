largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
area = largura * altura
tinta = area / 2

print(f"Na parece de largura {largura} x {altura} com área total de {area}m² "
      f"\nvai utilizar {tinta:.2f} litros de tinta. ")

#Resolução guanabara

# larg = float(input("Largura da parede: "))
# alt = float(input("Altura da parede: "))
# area = larg * alt
#
# print("Sua parede tem a dimensão de  {} x {} e a sua área é de {}m².".format(larg, alt , area))
# tinta = area / 2
# print("Para pintar essa parede, você precisarar de {}l de tinta. ".format(tinta))