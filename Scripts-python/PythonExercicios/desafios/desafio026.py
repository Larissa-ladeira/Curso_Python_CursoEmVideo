frase = input("Digite uma frase: ").strip().upper()

quantidade = frase.lower().count("A")
primeira = frase.find("a")
ultima = frase.rfind("a")

print(f"A frase {frase} "
      f"\nA letra A apareceu {quantidade} vezes."
      f"\nA primeira letra a aparece na posição {primeira} "
      f"\nA última letra a aparece na posição {ultima + 1} ")