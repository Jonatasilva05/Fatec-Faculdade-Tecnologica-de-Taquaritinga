# LISTA DOS CANDIDATOS INFORMADOS
candidatos = ["Fulano", "Beltrano", "Ciclano"]

# DICIONARIO/LISTA PARA INFORMAR A FAIXA ETARIA
faixa_etaria = {
    "1": [0, 0, 0],  # AQUI É DE 16-18 anos
    "2": [0, 0, 0],  # AQUI É DE 19-22 anos
    "3": [0, 0, 0],  # AQUI É DE 23-25 anos
    "4": [0, 0, 0]   # AQUI É DE 26+ anos
}

# DICIONARIO/LISTA PARA INFORMAR O GENERO
genero = {"m": [0, 0, 0], "f": [0, 0, 0], "outro": [0, 0, 0]}

faixa_etaria_labels = {
    "1": "16-18 anos",
    "2": "19-22 anos",
    "3": "23-25 anos",
    "4": "26+ anos"
}

# NUMERO TOTAL DE VOTOS COMPUTADOS
total_votos = 0

# FUNÇÃO QUE IRÁ REALIZAR A VOTAÇÃO
def registrar_voto():
    global total_votos
    
    print("\nVotacao para representante de sala!")
    print("1 - Fulano\n 2 - Beltrano\n 3 - Ciclano")
    
    # try FUNCIONA COMO UM "ALERTA DE ERRO" OU SEJA, ELE SÓ IRÁ SER CHAMADO/ATIVADO, QUANDO HOUVER ALGUMA AÇÃO QUE NÃO FAZ PARTE DO CODIGO
    # NESSE CASO ELE ESTA SENDO ULTILIZADO PARA SE CASO O USUARIO DIGITAR ALGUM NUMERO QUE NÃO SEJA ENTRE 1 2 E 3, ELE IRÁ INFORMAR O PRINT DE ERRO "print("Numero inválido. Digite um número válido.")"
    try:
        voto = int(input("Digite o número do candidato escolhido: ")) - 1
        if voto not in [0, 1, 2]:
            print("Opção inválida. Tente novamente.")
            return False
    except ValueError:
        print("Numero inválido. Digite um número válido.")
        return False
    
    # items() É PARA ARMAZENAR E RETORNAR O VALOR DAS TUPLAS OU SEJA, OS DADOS INFORMADOS DAS FAIXAS ETARIAS
    print("\nEscolha sua faixa etária:")
    for key, value in faixa_etaria_labels.items():
        print(f"{key}: {value}")
    
    # A "FUNÇÃO" strip() remove espaços em branco e caracteres iniciais e finais de uma string ou seja, se digitar com espaço em branco no final ou começo do valor não dará erro pois ele limpa automaticamente
    faixa = input("Digite o número correspondente ").strip()
    if faixa not in faixa_etaria:
        print("Faixa etária inválida. Tente novamente.")
        return False
    
    # lower() SERVE PARA CONVERTER A STRING OU SEJA, A LETRA EM MINUSCULA AUTOMATICAMENTE
    genero_input = input("Digite seu gênero: \n M - para masculino \n F - para feminino \n outro para outros): ").strip().lower()
    if genero_input not in genero:
        print("Gênero inválido. Tente novamente.")
        return False
    
    # AQUI FARÁ O REGISTRO DO VOTO
    faixa_etaria[faixa][voto] += 1
    genero[genero_input][voto] += 1
    total_votos += 1
    
    return True

# FUNCÃO PARA EXIBIR OS RESULTADOS CORRETOS E DETALHADOS
def exibir_resultados():
    print("\nResultados da votação:")
    
    if total_votos == 0:
        print("Nenhum voto registrado.")
        return
    
    # EXIBIRA AS FAIXAS ETARIAS DOS USUARIOS
    for faixa, votos in faixa_etaria.items():
        print(f"\nFaixa Etária {faixa_etaria_labels[faixa]}:")
        for i, candidato in enumerate(candidatos):
            percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
            print(f"  {candidato}: {percentual:.2f}% ({votos[i]} votos)")
    
    # EXIBE OS VOTOS POR GENERO
    for gen, votos in genero.items():
        print(f"\nGênero {gen.capitalize()}:")
        for i, candidato in enumerate(candidatos):
            percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
            print(f"  {candidato}: {percentual:.2f}% ({votos[i]} votos)")

# FUNÇÃO PRINCIPAL
def main():
    while True:
        if not registrar_voto():
            continue
        
        cont = input("Deseja registrar outro voto? (sim/não): ").strip().lower()
        if cont != "sim":
            break

    # EXIBIR OS RESULTADOS FINAIS
    exibir_resultados()

# EXECUTAR TODAS A ESTRUTURA
if __name__ == "__main__":
    main()