import pygame
from pygame.sprite import Sprite

class Missel(Sprite):

    def __init__(self, ia_game):
        super().__init__()
        self.screen = ia_game.screen
        self.settings = ia_game.settings

        # Carrega a imagem do míssil
        self.imagem = pygame.image.load('imagens/missil.png')  # Certifique-se de que o caminho da imagem está correto
        self.rect = self.imagem.get_rect()  # Obtém o rect da imagem do míssil
        self.rect.midtop = ia_game.nave.rect.midtop  # Posiciona o míssil no topo da nave

        # Armazena a posição vertical do míssil como float para movimentação suave
        self.y = float(self.rect.y)

    def update(self):
        """Move o míssil para cima na tela."""
        self.y -= self.settings.velocidade_missel  # Atualiza a posição do míssil, subindo na tela
        self.rect.y = self.y  # Atualiza o rect com a nova posição y

    def gerar_missel(self):
        """Desenha o míssil na tela na sua posição atual."""
        self.screen.blit(self.imagem, self.rect)  # Desenha a imagem do míssil na tela
