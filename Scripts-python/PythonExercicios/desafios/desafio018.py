import math

angulo = int(input("Digite o valor do ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O angulo {angulo} tem o seno {seno:.2f}"
      f"\ncosseno {cosseno:.2f}  "
      f"\ne tangente {tangente:.2f}")

#Resolução guanabara
# from math import radians, sin, cos, tan
# ângulo = float(input("Digite o ângulo que você deseja: "))
# seno = sin(math.radians(ângulo))
# print("O angulo {} tem o seno {:.2f}".format(ângulo, seno))
#
# cosseno = cos(math.radians(angulo))
# print("O angulo {} tem o seno {:.2f}".format(ângulo, cosseno))
#
# tangente = tan(math.radians(angulo))
# print("O angulo {} tem o seno {:.2f}".format(ângulo, tangente))



