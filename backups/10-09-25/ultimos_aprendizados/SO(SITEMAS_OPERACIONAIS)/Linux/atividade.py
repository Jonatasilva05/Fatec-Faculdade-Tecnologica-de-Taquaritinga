import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Na analogia do carro, o que o Linux representa em sua essência?",
        "opcoes": {
            "A": "O carro completo, pronto para dirigir.",
            "B": "Apenas o motor (o kernel).",
            "C": "Apenas as rodas e o volante.",
            "D": "O motorista."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Quem é o criador do kernel Linux e em que ano o projeto foi iniciado?",
        "opcoes": {
            "A": "Richard Stallman, em 1985.",
            "B": "Bill Gates, em 1995.",
            "C": "Linus Torvalds, em 1991.",
            "D": "Steve Jobs, em 1984."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Quando um amigo diz que 'instalou o Linux', o que ele tecnicamente instalou no computador?",
        "opcoes": {
            "A": "Apenas o kernel, sem interface gráfica ou programas.",
            "B": "O sistema operacional Android.",
            "C": "Uma 'distribuição', que é o kernel Linux mais um conjunto de programas e interface.",
            "D": "Uma versão de testes do sistema MINIX."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Qual foi uma das principais motivações de Linus Torvalds para criar o seu próprio kernel?",
        "opcoes": {
            "A": "Ele queria criar um sistema para vender e competir com a Microsoft.",
            "B": "O sistema UNIX era muito caro e a alternativa, MINIX, era limitada e não podia ser modificada livremente.",
            "C": "Ele recebeu um contrato de uma grande empresa para desenvolver um novo sistema.",
            "D": "Ele queria criar um sistema operacional exclusivo para servidores de internet."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Qual era a 'peça que faltava' no Projeto GNU, de Richard Stallman, que o kernel Linux preencheu perfeitamente?",
        "opcoes": {
            "A": "Um editor de texto.",
            "B": "Uma interface gráfica.",
            "C": "O kernel.",
            "D": "Um navegador de internet."
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Qual sistema operacional, presente na maioria dos smartphones, é um exemplo famoso de uso do kernel Linux?",
        "opcoes": {
            "A": "iOS",
            "B": "Android",
            "C": "Windows Phone",
            "D": "Symbian"
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
janela.title("Quiz: Fundamentos do Linux")
janela.geometry("500x500")

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