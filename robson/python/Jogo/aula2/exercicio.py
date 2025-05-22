numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º numero: "))
    numeros.append(numero)

#(f"Digite .....") a letra f serve para representar uma estrutura de repetição
#append serve para anexar um elemento ao final da lista

NumMaior = max(numeros)
NumMenor = min(numeros)
#a "função" max serve para retornar o maior numero, ou seja uma "busca" pelo maior numero digitado presente na lista
#a "função" min serve para retornar o menor numero, ou seja uma "busca" pelo menor numero digitado presente na lista

posiMaior = [i for i, v in enumerate(numeros) if v == NumMaior]
#enumerate permite ter um loop e contador automatico
posiMenor = [i for i, v in enumerate(numeros) if v == NumMenor]

print(f"\nLista de numeros: {numeros}")
#\n é quebra de linha, para que os proximos print nao apareça um "grudado" no outro
print(f"O maior numero é {NumMaior} e esta na posição {posiMaior}")
print(f"O menor numero é {NumMenor} e esta na posição {posiMenor}")