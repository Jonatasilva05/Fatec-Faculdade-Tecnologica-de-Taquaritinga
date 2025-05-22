import pygame

class Nave:
    def __init__(self, ia_game):
        """Inicializa a nave e define sua posição inicial."""
        self.screen = ia_game.screen
        self.screen_rect = ia_game.screen.get_rect()
        
        
        #Carrega a imagem
        self.imagem = pygame.image.load('imagens/nave.bmp')
        self.rect = self.imagem.get_rect()

        #Coloca imgem da nave no centro da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Coloca a nave na localização atual"""
        self.screen.blit(self.imagem, self.rect)