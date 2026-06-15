import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Qual é o problema clássico na área de tecnologia que o Docker ajuda a resolver?",
        "opcoes": {
            "A": "A internet está muito lenta.",
            "B": "O computador não tem memória suficiente.",
            "C": "'Funciona na minha máquina!'",
            "D": "O monitor não está ligando."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Na analogia dos contêineres de navio, o que o Docker faz para o software?",
        "opcoes": {
            "A": "Aumenta a velocidade do software, como um navio mais rápido.",
            "B": "Transporta o software em caixas de tamanhos diferentes e desorganizadas.",
            "C": "Empacota o software em uma 'caixa' padronizada que roda em qualquer lugar.",
            "D": "Atua como o guindaste, movendo apenas partes do software."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "O que um 'contêiner' Docker empacota dentro dele?",
        "opcoes": {
            "A": "Apenas o código-fonte da aplicação.",
            "B": "O aplicativo com TUDO o que ele precisa para funcionar (código, ferramentas, bibliotecas, etc.).",
            "C": "Somente o banco de dados que a aplicação utiliza.",
            "D": "Apenas as imagens e os vídeos da aplicação."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "O Docker Hub, onde imagens são compartilhadas, é frequentemente comparado a qual outra plataforma?",
        "opcoes": {
            "A": "Uma loja de aplicativos como a Play Store, mas para servidores.",
            "B": "Uma plataforma de streaming como a Netflix.",
            "C": "Um editor de texto como o Bloco de Notas.",
            "D": "Uma rede social para desenvolvedores."
        },
        "resposta_correta": "A"
    },
    {
        "pergunta": "No Docker Hub, o que são as 'Imagens Oficiais'?",
        "opcoes": {
            "A": "São as imagens mais caras disponíveis para compra.",
            "B": "São imagens criadas por qualquer pessoa da comunidade.",
            "C": "São imagens mantidas e verificadas pela própria Docker ou pelos criadores do software.",
            "D": "São as imagens que funcionam apenas no sistema operacional Linux."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Para uma imagem como 'node:18-alpine', o que a parte ':18-alpine' significa?",
        "opcoes": {
            "A": "O número de vezes que a imagem foi baixada.",
            "B": "Uma 'tag', que especifica a versão e o 'sabor' da imagem.",
            "C": "O nome do desenvolvedor que criou a imagem.",
            "D": "A data em que a imagem foi criada."
        },
        "resposta_correta": "B"
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
janela.title("Quiz sobre Docker: Conceitos Fundamentais")
janela.geometry("500x420") # Ajustei a altura para caber melhor o conteúdo

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