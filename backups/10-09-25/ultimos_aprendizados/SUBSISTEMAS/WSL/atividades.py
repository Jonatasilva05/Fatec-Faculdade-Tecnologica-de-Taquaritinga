import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Qual analogia descreve melhor o funcionamento do WSL (Subsistema do Windows para Linux)?",
        "opcoes": {
            "A": "Uma 'casa de hóspedes' pesada dentro da sua casa (Máquina Virtual).",
            "B": "Duas casas separadas, exigindo sair de uma para entrar na outra (Dual Boot).",
            "C": "Uma 'porta mágica' que conecta sua casa (Windows) a uma oficina (Linux).",
            "D": "Um segundo computador dedicado apenas para o Linux."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Qual é a principal e maior vantagem de usar o WSL, conforme destacado nos textos?",
        "opcoes": {
            "A": "O isolamento completo do Windows para máxima segurança.",
            "B": "A integração perfeita, permitindo usar ferramentas Linux e apps do Windows no mesmo fluxo de trabalho.",
            "C": "O suporte a aplicações gráficas (GUI) mais estável que no Linux nativo.",
            "D": "O acesso direto e de baixo nível ao hardware do computador."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Qual foi a grande evolução introduzida com o WSL 2 em 2019?",
        "opcoes": {
            "A": "Foi a primeira versão a permitir a instalação do Ubuntu.",
            "B": "Abandonou a linha de comando para focar apenas em interfaces gráficas.",
            "C": "Passou a traduzir comandos Linux para o Windows de forma mais lenta.",
            "D": "Passou a usar um kernel Linux de verdade, garantindo mais velocidade e compatibilidade."
        },
        "resposta_correta": "D"
    },
    {
        "pergunta": "Para um desenvolvedor que valoriza iniciar o ambiente rapidamente e com baixo consumo de memória, qual é a melhor solução?",
        "opcoes": {
            "A": "Instalar uma Máquina Virtual (VM) completa.",
            "B": "Configurar um dual boot com Windows e Ubuntu.",
            "C": "Comprar um segundo computador para rodar Linux.",
            "D": "Usar o WSL 2."
        },
        "resposta_correta": "D"
    },
    {
        "pergunta": "Qual dos cenários abaixo é um caso de uso ideal para o WSL?",
        "opcoes": {
            "A": "Um desenvolvedor web que precisa replicar o ambiente de um servidor Linux em sua máquina Windows.",
            "B": "Um usuário que precisa gerenciar as partições de disco do computador.",
            "C": "Um designer que precisa rodar a suíte Adobe com interface gráfica no Linux.",
            "D": "Um gamer que quer obter o máximo de desempenho gráfico para jogos."
        },
        "resposta_correta": "A"
    },
    {
        "pergunta": "Qual é uma das desvantagens ou limitações conhecidas do WSL?",
        "opcoes": {
            "A": "Ele consome muito mais memória RAM que uma Máquina Virtual completa.",
            "B": "É impossível acessar os arquivos do Windows de dentro do ambiente Linux.",
            "C": "Não é ideal para tarefas que exigem acesso direto e de baixo nível ao hardware.",
            "D": "Não é compatível com ferramentas populares como Docker ou Git."
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
janela.title("Quiz: Dominando o WSL")
janela.geometry("500x520")

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