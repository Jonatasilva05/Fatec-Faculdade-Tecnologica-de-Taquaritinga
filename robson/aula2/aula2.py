numeros = []  # Lista para armazenar os números

# Lendo os 5 valores numéricos e armazenando na lista
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Inicializando maior e menor com os primeiros valores da lista
maior = max(numeros)
menor = min(numeros)

# Encontrando as posições do maior e menor número
posicoes_maior = [i for i, v in enumerate(numeros) if v == maior]
posicoes_menor = [i for i, v in enumerate(numeros) if v == menor]

# Exibindo os resultados
print(f"\nLista de números: {numeros}")
print(f"O maior número é {maior} e está na posição {posicoes_maior}")
print(f"O menor número é {menor} e está na posição {posicoes_menor}")
