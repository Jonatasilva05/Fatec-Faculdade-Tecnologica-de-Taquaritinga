import tkinter as tk
from tkinter import messagebox

# --- DADOS DO QUIZ BASEADOS NOS SEUS ARQUIVOS ---
# Lista de perguntas, onde cada pergunta é um dicionário
perguntas = [
    {
        "pergunta": "Qual famoso desafio técnico, relacionado a lidar com 10.000 conexões simultâneas, motivou a criação do NGINX?",
        "opcoes": {
            "A": "O problema do \"bug do milênio\" (Y2K)",
            "B": "O problema C10k",
            "C": "O desafio de criar o primeiro servidor web",
            "D": "O problema de falta de memória nos servidores"
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Na analogia do restaurante, o que torna o NGINX um 'garçom' tão eficiente?",
        "opcoes": {
            "A": "Ele dedica um garçom exclusivo para cada mesa, que fica esperando ao lado dela.",
            "B": "Ele atua como um único 'super garçom' que anota pedidos de várias mesas sem precisar esperar.",
            "C": "Ele só trabalha em restaurantes com um único tipo de prato.",
            "D": "Ele atua como o cozinheiro que prepara todos os pedidos."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Quando o NGINX atua como um 'recepcionista' de escritório, protegendo e organizando o acesso aos servidores internos, qual função ele está desempenhando?",
        "opcoes": {
            "A": "Cache de Conteúdo",
            "B": "Servidor Web",
            "C": "Proxy Reverso",
            "D": "Balanceador de Carga"
        },
        "resposta_correta": "C"
    },
    {
        "pergunta": "Para um e-commerce na Black Friday que usa vários servidores, qual função do NGINX é ESSENCIAL para distribuir o tráfego e evitar que o site caia?",
        "opcoes": {
            "A": "Balanceador de Carga (Load Balancer)",
            "B": "A arquitetura orientada a eventos",
            "C": "Cache de Conteúdo",
            "D": "Proxy Reverso"
        },
        "resposta_correta": "A"
    },
    {
        "pergunta": "Qual é o 'segredo técnico' por trás da alta eficiência e baixo consumo de memória do NGINX?",
        "opcoes": {
            "A": "O uso de um processo dedicado para cada conexão, garantindo atenção total.",
            "B": "Sua arquitetura orientada a eventos (assíncrona e não-bloqueante).",
            "C": "A exigência de servidores com hardware muito mais potente.",
            "D": "Sua capacidade de funcionar apenas com conteúdo estático."
        },
        "resposta_correta": "B"
    },
    {
        "pergunta": "Quando o NGINX guarda cópias de arquivos populares para entregá-los instantaneamente, agindo como um 'barista esperto', qual função ele está usando?",
        "opcoes": {
            "A": "Balanceador de Carga",
            "B": "Proxy Reverso",
            "C": "Servidor Web",
            "D": "Cache de Conteúdo"
        },
        "resposta_correta": "D"
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
janela.title("Quiz: Fundamentos do NGINX")
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