import pygame.font
from pygame.sprite import Group

from nave import Nave


class Pontuacao:
    """Uma classe para registrar as informações de pontuação."""

    def __init__(self, ia_game):
        """Inicializar atributos de pontuação."""
        self.ia_game = ia_game
        self.screen = ia_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ia_game.settings
        self.estatisticas = ia_game.estatisticas

        # Formatação do texto.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_pontuacao_maxima()
        self.prep_fase()
        self.prep_naves()

    def prep_score(self):
        """Transforma a pontuaçaõ numa imagem renderizada."""
        pontos_arredondados = round(self.estatisticas.score, -1)
        score_txt = f"{pontos_arredondados:,}"
        self.score_image = self.font.render(score_txt, True,
                self.text_color, self.settings.bg_color)

        # Mostra a pontuação no canto direito da tela.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_pontuacao_maxima(self):
        """Transforma a pontuação máxima numa imagem renderizada."""
        pontuacao_maxima = round(self.estatisticas.pontuacao_maxima, -1)
        pontuacao_maxima_txt = f"{pontuacao_maxima:,}"
        self.high_score_image = self.font.render(pontuacao_maxima_txt, True,
                self.text_color, self.settings.bg_color)
        
        # Mostra a pontuação máxima no centro da tela no topo.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_fase(self):
        """Transforma a fase numa imagem renderizada."""
        fase_txt = str(self.estatisticas.level)
        self.level_image = self.font.render(fase_txt, True,
                self.text_color, self.settings.bg_color)

        # Mostra a fase abaixo da pontuacao.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_naves(self):
        """Mostra quantas naves/vidas ainda restam."""
        self.nave = Group()
        for num_nave in range(self.estatisticas.naves_restantes):
            nave = Nave(self.ia_game)
            nave.rect.x = 10 + num_nave * nave.rect.width
            nave.rect.y = 10
            self.nave.add(nave)

    def checa_pontuacao_maxima(self):
        """Verifica se tem uma nova pontuacao maxima."""
        if self.estatisticas.score > self.estatisticas.pontuacao_maxima:
            self.estatisticas.pontuacao_maxima = self.estatisticas.score
            self.prep_pontuacao_maxima()

    def mostra_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.nave.draw(self.screen)