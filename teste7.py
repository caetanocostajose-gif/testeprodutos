produtos = ["arroz", "feijão","café", "açúcar"]

produtos[1] = "pão" 
produtos.remove("café")
if "leite" in produtos:
    produtos.remove("leite")
else:
    print("O produto leite não está na lista.")

print(produtos)