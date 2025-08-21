import pygame
from pygame.sprite import Sprite

class Nave(Sprite):
    def __init__(self, ia_game):
        """Inicializa a nave e define sua posição inicial."""
        super().__init__()
        self.screen = ia_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ia_game.settings  # Acesso às configurações

        # Carrega a imagem da nave
        self.image = pygame.image.load('imagens/bem.bmp')  # Corrigido para 'image'
        self.rect = self.image.get_rect()

        # Coloca imagem da nave no centro da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena a posição decimal da nave
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Flags de movimento
        self.mover_direita = False
        self.mover_esquerda = False
        self.mover_cima = False
        self.mover_baixo = False

    def update(self):
        """Atualiza a posição da nave com base nas flags de movimento."""
        if self.mover_direita and self.rect.right < self.screen_rect.right:
            self.x += self.settings.velocidade_nave
        if self.mover_esquerda and self.rect.left > 0:
            self.x -= self.settings.velocidade_nave
        if self.mover_cima and self.rect.top > 0:
            self.y -= self.settings.velocidade_nave
        if self.mover_baixo and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.velocidade_nave

        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Desenha a nave em sua posição atual."""
        self.screen.blit(self.image, self.rect)  # Corrigido para 'image'

    def centraliza_nave(self):
        """Centraliza a nave na tela."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
