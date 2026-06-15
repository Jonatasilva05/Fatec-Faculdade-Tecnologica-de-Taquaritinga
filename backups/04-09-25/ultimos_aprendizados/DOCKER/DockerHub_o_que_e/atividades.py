import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "De acordo com as analogias nos textos, o que é o Docker Hub?",
        "opcoes": {
            "A": "Uma fábrica para criar softwares complexos do zero.",
            "B": "Uma \"loja de blocos\" ou um \"GitHub\" para imagens Docker prontas.",
            "C": "Um sistema operacional para rodar contêineres.",
            "D": "Uma ferramenta para escrever código em Python."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Qual é a maneira mais eficiente ('o jeito Docker') de obter e usar um software como o Redis sem instalá-lo manualmente?",
        "opcoes": {
            "A": "Baixar o código-fonte e compilá-lo no seu computador.",
            "B": "Procurar a imagem oficial no Docker Hub e executá-la com um comando.",
            "C": "Pedir para um colega de equipe instalar para você.",
            "D": "Comprar um servidor que já venha com o Redis."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Ao buscar por uma imagem (ex: PostgreSQL), qual o principal fator para escolher a versão mais segura e confiável?",
        "opcoes": {
            "A": "A que tem o maior número de downloads.",
            "B": "A que foi criada pelo usuário com o nome mais interessante.",
            "C": "A que possui o selo \"Official Image\" (Imagem Oficial).",
            "D": "A que tem a descrição mais longa e detalhada."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "O que são as 'tags' em uma imagem Docker, como em 'node:18-alpine'?",
        "opcoes": {
            "A": "O preço que você deve pagar pela imagem.",
            "B": "Comentários e avaliações de outros usuários.",
            "C": "O nome do criador da imagem.",
            "D": "As 'versões' ou 'sabores' da imagem, que definem a versão do software."
        },
        "resposta_correta": "D"
    },
    {
        "pergunta": "Qual a principal diferença entre 'Imagens Oficiais' e 'Imagens da Comunidade'?",
        "opcoes": {
            "A": "Oficiais são pagas; da comunidade são gratuitas.",
            "B": "Oficiais são mantidas e verificadas (mais seguras); da comunidade são criadas por qualquer um.",
            "C": "Da comunidade são sempre mais leves e rápidas.",
            "D": "Não há nenhuma diferença prática entre elas."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "O que é o 'Docker ID' que você define ao criar uma conta no Docker Hub?",
        "opcoes": {
            "A": "Seu endereço de e-mail.",
            "B": "Uma senha temporária gerada pelo site.",
            "C": "Seu nome de usuário único, usado para identificar suas próprias imagens.",
            "D": "Um número de identificação do seu computador."
        },
        "resposta_correta": "C"
    }
]


# Variáveis para controlar o estado do quiz
pergunta_atual_index = 0
pontuacao = 0

# --- FUNÇÕES DO QUIZ ---

def carregar_pergunta():
    """Limpa as opções antigas e carrega a pergunta e opções atuais."""
    global pergunta_atual_index
    
    for widget in frame_opcoes.winfo_children():
        widget.destroy()

    pergunta_info = perguntas[pergunta_atual_index]
    label_pergunta.config(text=pergunta_info["pergunta"])
    escolha_usuario.set(None)

    for opcao, texto in pergunta_info["opcoes"].items():
        radio_botao = tk.Radiobutton(
            frame_opcoes,
            text=f"{opcao}) {texto}",
            variable=escolha_usuario,
            value=opcao,
            font=("Arial", 10),
            wraplength=450,
            justify=tk.LEFT
        )
        radio_botao.pack(anchor="w", pady=2)

def verificar_resposta():
    """ Pega a resposta selecionada, compara com a correta e avança para a próxima pergunta. """
    global pergunta_atual_index, pontuacao

    resposta_selecionada = escolha_usuario.get()
    
    if not resposta_selecionada or resposta_selecionada == 'None':
        messagebox.showwarning("Atenção!", "Por favor, selecione uma opção antes de verificar.")
        return

    pergunta_info = perguntas[pergunta_atual_index]
    if resposta_selecionada == pergunta_info["resposta_correta"]:
        pontuacao += 1
        messagebox.showinfo("Correto!", "Você acertou! ✅")
    else:
        resposta_correta = pergunta_info["resposta_correta"]
        texto_resposta_correta = pergunta_info["opcoes"][resposta_correta]
        msg = f"Incorreto. ❌\nA resposta correta era: {resposta_correta}) {texto_resposta_correta}"
        messagebox.showerror("Incorreto", msg)
    
    pergunta_atual_index += 1

    if pergunta_atual_index < len(perguntas):
        carregar_pergunta()
    else:
        messagebox.showinfo("Fim do Quiz", f"Quiz finalizado!\n\nSua pontuação final é: {pontuacao}/{len(perguntas)}")
        janela.destroy()

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Quiz: Explorando o Docker Hub")
janela.geometry("500x480")

# --- CRIAÇÃO DOS COMPONENTES (WIDGETS) ---

label_pergunta = tk.Label(janela, text="", wraplength=480, justify=tk.LEFT, font=("Arial", 12, "bold"))
label_pergunta.pack(pady=(10, 20), padx=10)

frame_opcoes = tk.Frame(janela)
frame_opcoes.pack(padx=20)

escolha_usuario = tk.StringVar()
escolha_usuario.set(None)

botao_verificar = tk.Button(janela, text="Verificar Resposta", command=verificar_resposta, font=("Arial", 10, "bold"))
botao_verificar.pack(pady=20)

# --- INICIA O QUIZ ---
carregar_pergunta()
janela.mainloop()