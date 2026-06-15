import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Na analogia da casa, o que um Contêiner representa?",
        "opcoes": {
            "A": "Um apartamento completo e totalmente independente.",
            "B": "A casa principal inteira.",
            "C": "Apenas um quarto que utiliza os recursos da casa principal.",
            "D": "O arquiteto que constrói a casa."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Qual software é o principal responsável por criar e gerenciar Máquinas Virtuais (VMs)?",
        "opcoes": {
            "A": "Motor de Container (Docker)",
            "B": "Kernel do Sistema Operacional",
            "C": "Hypervisor",
            "D": "WSL (Subsistema do Windows para Linux)"
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Qual é a principal diferença de tamanho e velocidade entre VMs e Contêineres?",
        "opcoes": {
            "A": "VMs são mais leves (MB) e rápidas (segundos).",
            "B": "Contêineres são muito mais pesados (GB) e lentos (minutos).",
            "C": "Não há diferença significativa de tamanho ou velocidade.",
            "D": "Contêineres são muito mais leves (MB) e rápidos (segundos)."
        },
        "resposta_correta": "D"
    },
    {
        "pergunta": "Cenário 1: Para analisar um arquivo suspeito (possível vírus) com o máximo de segurança e isolamento, qual a melhor escolha?",
        "opcoes": {
            "A": "Uma Máquina Virtual (VM), para garantir isolamento total.",
            "B": "Um Contêiner, pois ele inicia mais rápido.",
            "C": "Executar diretamente na máquina principal.",
            "D": "Ambos oferecem o mesmo nível de segurança."
        },
        "resposta_correta": "A"
    },
    {
        "pergunta": "Cenário 2: Uma empresa quer modernizar sua aplicação dividindo-a em 10 'microsserviços' para otimizar recursos. Qual a abordagem mais eficiente?",
        "opcoes": {
            "A": "Criar 10 VMs pesadas, uma para cada serviço.",
            "B": "Usar Contêineres para rodar cada serviço de forma leve e isolada.",
            "C": "Comprar 10 servidores físicos diferentes.",
            "D": "Rodar tudo junto no mesmo sistema, sem isolamento."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Com base na arquitetura mostrada nas imagens, qual camada existe em uma VM mas NÃO existe em um Contêiner?",
        "opcoes": {
            "A": "A Aplicação (App).",
            "B": "As Bibliotecas (Bins/Libs).",
            "C": "Um Sistema Operacional Convidado (Guest OS) próprio.",
            "D": "A Infraestrutura (Hardware)."
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
janela.title("Quiz: VMs vs. Contêineres")
janela.geometry("500x450")

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