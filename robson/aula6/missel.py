import pygame 
from pygame.sprite import Sprite  #importa a classe Sprite, que serve como base para o objeto missel

class Missel(Sprite):
    # classe que representa um míssil disparado pela nave, herda de Sprite

    def __init__(self, ia_game):
        # inicializa o míssil e define sua posição inicial
        
        super().__init__() # chama o construtor da classe mãe (Sprite)
        self.screen = ia_game.screen # Obtém a tela de jogo para onde o missil sera desenhado
        self.settings = ia_game.settings # acessa as configurações do jogo, incluindo velocidade e cor do missil
        self.color = self.settings.cor_missel # define a cor do missil a partir das configurações
        self.rect = pygame.Rect(0, 0, self.settings.largura_missel, self.settings.altura_missel)

        self.rect.midtop = ia_game.nave.rect.midtop

        self.y = float(self.rect.y)