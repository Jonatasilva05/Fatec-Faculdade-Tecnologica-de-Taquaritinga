import pygame

class Nave:
    def __init__(self, ia_game):
        """Inicializa a nave e define sua posição inicial."""
        self.screen = ia_game.screen
        self.screen_rect = ia_game.screen.get_rect()
        self.settings = ia_game.settings #Adicionando o acesso ás configurações
        
        
        #Carrega a imagem
        self.imagem = pygame.image.load('imagens/nave.bmp')
        self.rect = self.imagem.get_rect()

        #Coloca imgem da nave no centro da tela
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.mover_direita = False
        self.mover_esquerda = False

    def blitme(self):
        """Coloca a nave na localização atual"""
        self.screen.blit(self.imagem, self.rect)

    def update(self):
        if self.mover_direita and self.rect.right < self.screen_rect.right:
            self.x += self.settings.velocidade_nave
        if self.mover_esquerda and self.rect.left > 0:
            self.x -= self.settings.velocidade_nave

        self.rect.x = self.x