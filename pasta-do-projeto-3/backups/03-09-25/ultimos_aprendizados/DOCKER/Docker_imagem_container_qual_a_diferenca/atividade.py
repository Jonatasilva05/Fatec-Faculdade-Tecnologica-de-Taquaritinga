import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Na analogia do bolo, o que a Imagem Docker representa?",
        "opcoes": {
            "A": "O bolo pronto e comestível",
            "B": "A receita com todos os ingredientes e o modo de preparo",
            "C": "A pessoa que come o bolo",
            "D": "A cozinha onde o bolo é feito"
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Qual das seguintes afirmações descreve corretamente um Contêiner Docker?",
        "opcoes": {
            "A": "É um template estático e imutável que nunca muda.",
            "B": "É uma instância 'viva' e em execução de uma imagem.",
            "C": "É o mesmo que uma máquina virtual.",
            "D": "É o arquivo de texto que define as dependências."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "O Docker Hub é frequentemente comparado a qual outra plataforma famosa?",
        "opcoes": {
            "A": "Netflix, para streaming de vídeos de tecnologia.",
            "B": "GitHub, mas para imagens Docker em vez de código.",
            "C": "Google Drive, para armazenar arquivos pessoais.",
            "D": "Amazon, para comprar servidores físicos."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "No Docker Hub, o que o selo 'Official Image' (Imagem Oficial) indica?",
        "opcoes": {
            "A": "Que a imagem é a mais baixada da plataforma.",
            "B": "Que a imagem é paga e requer uma assinatura.",
            "C": "Que a imagem é mantida e verificada pela Docker ou pelos criadores do software.",
            "D": "Que a imagem foi criada por um membro da comunidade."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Se você precisa de uma versão específica de uma imagem, como `node:18-alpine`, o que a parte '18-alpine' representa?",
        "opcoes": {
            "A": "O preço da imagem.",
            "B": "O nome do criador da imagem.",
            "C": "Uma 'tag', que especifica a versão e a base do sistema operacional.",
            "D": "Um comando para deletar a imagem."
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
    
    # Limpa os botões de rádio da pergunta anterior
    for widget in frame_opcoes.winfo_children():
        widget.destroy()

    # Pega a pergunta atual da lista
    pergunta_info = perguntas[pergunta_atual_index]

    # Atualiza o texto da pergunta
    label_pergunta.config(text=pergunta_info["pergunta"])

    # Garante que nenhuma opção venha pré-selecionada
    escolha_usuario.set(None)

    # Cria os novos botões de rádio para a pergunta atual
    for opcao, texto in pergunta_info["opcoes"].items():
        radio_botao = tk.Radiobutton(
            frame_opcoes,
            text=f"{opcao}) {texto}", # Adiciona a letra da opção para clareza
            variable=escolha_usuario,
            value=opcao,
            font=("Arial", 10),
            wraplength=450, # Quebra de linha para textos longos
            justify=tk.LEFT
        )
        radio_botao.pack(anchor="w", pady=2)

def verificar_resposta():
    """ Pega a resposta selecionada, compara com a correta e avança para a próxima pergunta. """
    global pergunta_atual_index, pontuacao

    resposta_selecionada = escolha_usuario.get()
    
    # Verifica se o usuário selecionou alguma opção
    if not resposta_selecionada or resposta_selecionada == 'None':
        messagebox.showwarning("Atenção!", "Por favor, selecione uma opção antes de verificar.")
        return

    # Compara a resposta
    pergunta_info = perguntas[pergunta_atual_index]
    if resposta_selecionada == pergunta_info["resposta_correta"]:
        pontuacao += 1
        messagebox.showinfo("Correto!", "Você acertou! ✅")
    else:
        resposta_correta = pergunta_info["resposta_correta"]
        texto_resposta_correta = pergunta_info["opcoes"][resposta_correta]
        msg = f"Incorreto. ❌\nA resposta correta era: {resposta_correta}) {texto_resposta_correta}"
        messagebox.showerror("Incorreto", msg)
    
    # Avança para a próxima pergunta
    pergunta_atual_index += 1

    # Verifica se o quiz terminou
    if pergunta_atual_index < len(perguntas):
        carregar_pergunta()
    else:
        messagebox.showinfo("Fim do Quiz", f"Quiz finalizado!\n\nSua pontuação final é: {pontuacao}/{len(perguntas)}")
        janela.destroy()

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Quiz sobre Docker")
janela.geometry("500x400") # Aumentei a altura para caber melhor as opções

# --- CRIAÇÃO DOS COMPONENTES (WIDGETS) ---

label_pergunta = tk.Label(janela, text="", wraplength=480, justify=tk.LEFT, font=("Arial", 12, "bold"))
label_pergunta.pack(pady=(10, 20), padx=10)

# Frame para agrupar os botões de rádio
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack(padx=20)

escolha_usuario = tk.StringVar()
escolha_usuario.set(None)

botao_verificar = tk.Button(janela, text="Verificar Resposta", command=verificar_resposta, font=("Arial", 10, "bold"))
botao_verificar.pack(pady=20)

# --- INICIA O QUIZ ---
carregar_pergunta()
janela.mainloop()