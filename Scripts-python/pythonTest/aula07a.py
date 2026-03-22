for c in range(3):
    print(f"--------Tentativa {c + 1} de 3 --------")
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2
    di = n1 // n2
    e = n1 ** n2
    print(f"Soma -> {n1} + {n2} = {s}")
    print(f"Multiplicação -> {n1} * {n2} = {m} e")
    print(f"Divisão -> {n1} / {n2} = {d}")
    print(f"Divisão real -> {n1} // {n2} = {di}")
    print(f"Exponenciação -> {n1} ** {n2} = {e}")