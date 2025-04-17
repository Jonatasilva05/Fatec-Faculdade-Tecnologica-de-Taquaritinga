import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ia_game):
        super().__init__()
        self.screen = ia_game.screen
        self.settings = ia_game.settings

        self.image = pygame.image.load('imagens/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.velocidade_alien * self.settings.direcao_frota
        self.rect.x = self.x

    def checar_borda(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

