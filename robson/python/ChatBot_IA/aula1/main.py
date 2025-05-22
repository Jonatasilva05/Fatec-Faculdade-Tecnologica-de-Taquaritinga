import time
import sys
import os

# FUNÇÃO PARA LIMPEZA DA TELA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNÇÃO PARA ANIMAÇÃO "DIGITAÇÃO" DAS LETRAS
def animar_texto(texto, delay=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# O "JOGO"
def jogo(nome_aventureiro, icone_personagem):
    limpar_tela()

    print(r"""
     ____    _______   ____    ____             ___        ___    __    ____     __   ____       ______
    |  _ \  |   ____| |    \  /    |           |   \      /   |  |  |  |    \   |  | |  __ \    /  __  \
    | |_| | |   ___   |     \/     |     ____   \   \    /   /   |  |  |     \  |  | | |  | |  |  |  |  |
    |  _ /  |   ___|  |  |\    /|  |    |____|   \   \  /   /    |  |  |  |\  \ |  | | |  | |  |  |  |  |
    | |_| | |  |____  |  | \__/ |  |              \   \/   /     |  |  |  | \  \|  | | |__| |  |  |__|  |
    |____/  |_______| |__|      |__|               \______/      |__|  |__|  \_____/ |_____/    \______/

    """)
    time.sleep(1)
    animar_texto(f"{nome_aventureiro} 💤 Ao ler um Livro de conto acabei adormecendo....")
    time.sleep(1)
    animar_texto(f"{nome_aventureiro} 🥱Acordei desorientado sem saber onde estava, então um velho me pergunta:")
    time.sleep(1)
    animar_texto("🧙‍♂️ Velho: Sabe onde está??")
    
    resposta = input("Digite 'sim' ou 'nao': ").strip().lower()

    if resposta == "nao":
        animar_texto("🧙‍♂️ : Você está em Doknoloand, um reino com muitos mistérios e uma caverna cheia de segredos poderosos a serem descobertos.")
        animar_texto("🧙‍♂️ : Deseja embarcar em uma aventura?")

        respostaOutra = input("Digite 'sim' ou 'nao': ").strip().lower()

        if respostaOutra == "nao":
            animar_texto(f"{icone_personagem} {nome_aventureiro}: Talvez em outra vida, aventureiro... 💤")
            exit()
        elif respostaOutra == "sim":
            animar_texto("🧙‍♂️ Velho: Primeiro, para saber se és digno, resolva o enigma...")
            animar_texto("🧙‍♂️ Velho: Sou leve como uma pena, mas nem o homem mais forte consegue me segurar por muito tempo.")

            respostaCorreta = input(f"{icone_personagem} {nome_aventureiro}: Minha resposta é... ").strip().lower()

            if respostaCorreta in ["folego", "fôlego", "Folego", "Fôlego" ]:
                animar_texto("🧙‍♂️ Velho: Você passou, parabéns...")
                animar_texto("✨ Embarcando...")
                animar_texto("✨ A CAVERNA ENCANTADA ✨")
                time.sleep(1)
                animar_texto("🌌 Entrando pelo portal Místico...\n")
                time.sleep(1)
                animar_texto("⚔️  Um novo aventureiro surge...")
                time.sleep(1)
                animar_texto("🌳  Em um mundo totalmente diferente, mais vivo, mais colorido...")
                time.sleep(1)
                animar_texto("🏔 Então um terremoto começa, o chão treme, as árvores balançam...")
                time.sleep(1)
                animar_texto(f"{icone_personagem} {nome_aventureiro}: Que isso??")
                time.sleep(1)
                animar_texto(f"{icone_personagem} {nome_aventureiro}: Quem é você??")
                time.sleep(1)
                animar_texto(r"""
                    _____
                   /     \\
                  | () () |
                   \  ^  /
                    |||||
                    |||||
                """)
                animar_texto(f"🧙‍♂️ Guardião: Seja muito bem-vindo, {nome_aventureiro}!")
                animar_texto("🧙‍♂️ Guardião: Eu sou o guardião da Caverna dos Segredos.")
                time.sleep(1)
                animar_texto("🧙‍♂️ Guardião: 🌟 Estou aqui para desejar que sua jornada seja repleta de sabedoria e coragem. Vai precisar 😈")
                print()
            else:
                animar_texto("🗡️ Você errou! Não és digno... Morra! 🗡️🩸")
                exit()
        else:
            animar_texto("Resposta inválida. Fim da jornada.")
            exit()
    else:
        animar_texto(f"{icone_personagem} {nome_aventureiro}: Então volte a dormir... 💀")
        exit()


# ESCOLHA DO GENERO
print("Escolha seu gênero:")
print("1 - Homem")
print("2 - Mulher")

genero = input("Digite o número correspondente: ").strip()

if genero == "1":
    icone_personagem = "🧝‍♂️"
    nome = input("Digite seu nome, bravo aventureiro: ")
elif genero == "2":
    icone_personagem = "🧝‍♀️"
    nome = input("Digite seu nome, corajosa aventureira: ")
else:
    print("Opção inválida. Encerrando o jogo.")
    exit()

jogo(nome, icone_personagem)
