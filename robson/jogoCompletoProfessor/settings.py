class Settings:
    def __init__(self):
        self.largura_tela = 1200
        self.altura_tela = 740
        self.bg_color = (230,230,230)

        #Configuração das naves
        self.naves_vida = 3

        #Configuração das balas
        self.largura_missel = 3
        self.altura_missel = 15
        self.cor_missel = (60, 60, 60)
        self.disparos_por_vez = 50

        #Configuração do alien
        self.velocidade_frota = 10

        #Velocidade que o jogo acelera
        self.aceleracao = 1.1

        self.valor_ponto = 1.5

        self.configuracoes_dinamicas()

    def configuracoes_dinamicas(self):
        """Inicializa as configurações que mudam ao longo do jogo."""
        self.velocidade_alien = 1.0
        self.velocidade_missel = 2.5
        self.velocidade_nave = 1.5

        # direção da fila onde 1 representa direita; -1 representa esquerda.
        self.direcao_frota = 1

        self.pontos_alien = 10

    def aumentar_velocidade(self):
        self.velocidade_nave *= self.aceleracao
        self.velocidade_missel *= self.aceleracao
        self.velocidade_alien *= self.aceleracao
        
        self.pontos_alien = int(self.pontos_alien * self.valor_ponto)

