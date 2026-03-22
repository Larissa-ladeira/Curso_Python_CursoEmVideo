tabuada = int(input("Digite um numero: "))
for t in range (10):
    print (f"{tabuada} x {t + 1:2} = {tabuada * (t+1)}")
#{t+1} soma os números para que a tabuada mostre de 1 a 10 ao invés
#     de 0 a 9 no {tabuada *(t+1)} multiplica o numero pelo numero da
#     linha atual EX: 5 X (0+1) = (5*1) 5x1=5


# Versão Guanabara
# num = int(input("Digite um numero para ver sua tabuada: "))
# print("-"*12)
# print('{} x {:2} = {:2}'.format(num, 1, num*1))
# print('{} x {:2} = {:2}'.format(num, 2, num*2))
# print('{} x {:2} = {:2}'.format(num, 3, num*3))
# print('{} x {:2} = {:2}'.format(num, 4, num*4))
# print('{} x {:2} = {:2}'.format(num, 5, num*5))
# print('{} x {:2} = {:2}'.format(num, 6, num*6))
# print('{} x {:2} = {:2}'.format(num, 7, num*7))
# print('{} x {:2} = {:2}'.format(num, 8, num*8))
# print('{} x {:2} = {:2}'.format(num, 9, num*9))
# print('{} x {:2} = {:2}'.format(num, 10, num*10))
# print("-"*12)
