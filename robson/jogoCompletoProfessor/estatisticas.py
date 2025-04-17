class Estatisticas:
    def __init__(self, ia_game):
        self.settings = ia_game.settings
        self.reset_estatisticas()

        # A pontuação mais alta nunca deve ser redefinida.
        self.pontuacao_maxima = 0

    def reset_estatisticas(self):
        self.naves_restantes = self.settings.naves_vida
        self.score = 0
        self.level = 1