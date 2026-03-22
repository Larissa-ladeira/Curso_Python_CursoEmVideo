import math

catetooposto = float(input("Digite o valor do cateto oposto: "))
catetoadjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = math.hypot(catetooposto, catetoadjacente)
print(f'no cateto oposto {catetooposto} e cateto adjacente {catetoadjacente} a hipotenusa é {hipotenusa:.2f}')


#Resolução guanabara
"""
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print("A hipotenusa vai medir: {:.2f}".format(hi))
"""

#2 resolução guanabara
"""
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)

print("O comprimento do cateto oposto:{}\nO comprimento do cateto adjacente: {} \nA hipotenusa vai medir: {:.2f}".format(co, ca, hi))
"""