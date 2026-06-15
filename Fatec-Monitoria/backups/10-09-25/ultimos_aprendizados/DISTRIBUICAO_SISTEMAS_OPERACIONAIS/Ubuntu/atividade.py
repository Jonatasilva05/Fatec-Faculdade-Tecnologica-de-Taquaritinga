import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ ---
# Agora temos uma lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Qual foi um dos principais diferenciais da primeira versão do Ubuntu, lançada em outubro de 2004?",
        "opcoes": {
            "A": "Ser gratuito, fácil de instalar e ter um ciclo previsível de lançamentos.",
            "B": "Ter a interface gráfica mais avançada da época.",
            "C": "Ser compatível apenas com computadores da marca Dell.",
            "D": "Ser um sistema pago, mas com suporte premium."
        },
        "resposta_correta": "A"
    },
    {
        "pergunta": "Qual lema representa melhor a filosofia do nome \"Ubuntu\", que significa \"humanidade para com os outros\"?",
        "opcoes": {
            "A": "\"Software livre para todos\"",
            "B": "\"O poder está na comunidade\"",
            "C": "\"Ninguém fica para trás\"",
            "D": "\"Simplesmente funciona\""
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Na analogia da casa:\nO Ubuntu é a casa pronta.\nO Linux é:",
        "opcoes": {
            "A": "A planta fundamental da estrutura",
            "B": "O endereço da casa",
            "C": "Os moradores"
        },
        "resposta_correta": "A"
    }
]

# Variáveis para controlar o estado do quiz
pergunta_atual_index = 0
pontuacao = 0

# --- FUNÇÕES DO QUIZ ---

def carregar_pergunta():
    """Limpa as opções antigas e carrega a pergunta e opções atuais."""
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
            text=texto,
            variable=escolha_usuario,
            value=opcao,
            font=("Arial", 10),
            justify=tk.LEFT
        )
        radio_botao.pack(anchor="w")

def verificar_resposta():
    """ Pega a resposta selecionada, compara com a correta e avança para a próxima pergunta. """
    global pergunta_atual_index, pontuacao

    resposta_selecionada = escolha_usuario.get()
    
    # Verifica se o usuário selecionou alguma opção
    if not resposta_selecionada:
        messagebox.showwarning("Atenção!", "Por favor, selecione uma opção antes de verificar.")
        return

    # Compara a resposta
    pergunta_info = perguntas[pergunta_atual_index]
    if resposta_selecionada == pergunta_info["resposta_correta"]:
        pontuacao += 1
        messagebox.showinfo("Correto!", "Você acertou! ✅")
    else:
        msg = f"Incorreto.\nA resposta correta era: {pergunta_info['resposta_correta']}"
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
janela.title("Quiz sobre Ubuntu")
janela.geometry("500x350")

# --- CRIAÇÃO DOS COMPONENTES (WIDGETS) ---

label_pergunta = tk.Label(janela, text="", wraplength=480, justify=tk.LEFT, font=("Arial", 12))
label_pergunta.pack(pady=(10, 20))

# Frame para agrupar os botões de rádio
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack()

escolha_usuario = tk.StringVar()

botao_verificar = tk.Button(janela, text="Verificar Resposta", command=verificar_resposta, font=("Arial", 10, "bold"))
botao_verificar.pack(pady=20)

# --- INICIA O QUIZ ---
carregar_pergunta()
janela.mainloop()