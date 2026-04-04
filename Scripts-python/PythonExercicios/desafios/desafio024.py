cidade = input("Digite o nome da cidade: ").strip()
santo = cidade[:5].lower() == "santo"

print(f"A cidade {cidade} começa com o nome santo? {santo}")