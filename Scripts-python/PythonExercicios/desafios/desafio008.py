# m = float(input ("Digite um valor em metros: "))

# quilometros = m * 0.001
# hecametros = m * 0.01
# decametros = m * 0.1
# decimetros = m * 10
# centimetros = m * 100
# milimetros = m * 1000

# print(f"{m:.1f} Metros corresponde a : {quilometros}km")
# print(f"{m:.1f} Metros corresponde a : {hecametros}hm")
# print(f"{m:.1f} Metros corresponde a : {decametros:.1f}dam")
# print(f"{m:.1f} Metros corresponde a : {decimetros:g}dm")
# print(f"{m:.1f} Metros corresponde a : {centimetros:g}cm")
# print(f"{m:.1f} Metros corresponde a : {milimetros:g}mm")

# 2º versão

m = float(input ("Digite um valor em metros: "))
print(f"{m:.1f}m corresponde a {m * 0.001}km")
print(f"{m:.1f}m corresponde a {m * 0.01}hm")
print(f"{m:.1f}m corresponde a {m * 0.1:.1f}dam")
print(f"{m:.1f}m corresponde a {m * 10:.0f}dm")
print(f"{m:.1f}m corresponde a {m * 100:.0f}cm")
print(f"{m:.1f}m corresponde a {m * 1000:.0f}mm")

#Resolução Guanabara
# m = float(input ("Distância em metros: "))
# cm = m * 100
# mm = m * 1000
# print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(m, cm, mm))
