# O import SERVE PARA IMPORTAR OU SEJA, CHAMAR AS BIBLIOTECAS INSTALADAS NESTE CASO CHAMANDO A sys E A pygame

import sys 
# A BIBLIOTECA sys SERVE PARA DAR ACESSO A VARIAVEIS E FUNÇÕES QUE INTERAGEM COM O INTERPRETADOR OU SEJA, ENTRE O PYTHON E O COMPUTADOR áveis e funções que interagem com o interpretador

import pygame
# A BIBLIOTECA pygame SERVE PARA CRIAR JOGOS 2D, APLICAÇÕES DE MULTIMIDIA, FAZER MANIPULAÇÃO DE IMAGENS E REPRODUZIR AUDIOS

from settings import Settings

from nave import Nave

# CRIA UMA classe CHAMADA InvasaoAlien
class InvasaoAlien:

    # O def CRIA UMA FUNÇÃO 
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        self.screen = pygame.display.set_mode((self.settings.largura_tela, self.settings.altura_tela))
        pygame.display.set_caption("Invasao Alien")
        self.nave = Nave(self)
        self.bg_color = (230,230,230) # COLOCANDO COR DE FUNDO CINZA

    def jogo_on(self):
        while True:
            def _checar_eventos(self):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.nave.blitme()

            # ATUALIZA A TELA
            pygame.display.flip()

            # CONTROLA A TAXA DE FRAMES POR SEGUNDO
            self.clock.tick(60) # NESTE CASO ESTA CONFIGURADO PARA FUNCIONAR A 60 FRAMES POR SEGUNDO

if __name__ == '__main__':
    ia = InvasaoAlien()
    ia.jogo_on()