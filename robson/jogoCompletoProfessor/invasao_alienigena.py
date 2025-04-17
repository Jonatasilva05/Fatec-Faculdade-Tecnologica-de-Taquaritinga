import sys
from time import sleep
import pygame

# Importando a classe de configurações
from settings import Settings
from estatisticas import Estatisticas
from pontuacao import Pontuacao
from botao import Botao
from nave import Nave
from missel import Missel
from alien import Alien


class InvasaoAlienigena:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Executando em tela cheia
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.largura_tela = self.screen.get_rect().width
        self.settings.altura_tela = self.screen.get_rect().height
        pygame.display.set_caption("Invasão Alienígena")

        self.estatisticas = Estatisticas(self)
        self.score = Pontuacao(self)
        self.nave = Nave(self)
        self.missel = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self._criar_frota()
        self.jogo_ativo = False

        self.botao_play = Botao(self, "Play")


    def jogo_on(self):
        while True:
            self._checar_eventos()

            if self.jogo_ativo:
                self.nave.update()
                self._atualiza_missel()  
                self._atualiza_aliens()

            self._atualiza_tela()
            self.clock.tick(60)



    def _checar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checar_teclaspress_eventos(event)
            elif event.type == pygame.KEYUP:
                self._checar_soltarteclas_eventos(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._checar_botao_play(mouse_pos)    

    def _checar_botao_play(self, mouse_pos):
        """Começa o jogo quando o usuário clica no play."""
        botao_clicado = self.botao_play.rect.collidepoint(mouse_pos)

        if botao_clicado and not self.jogo_ativo:
            #Redefine as configurações do jogo
            self.settings.configuracoes_dinamicas()

            # Zera a pontuação e estatisticas.
            self.estatisticas.reset_estatisticas()
            self.score.prep_score()
            self.score.prep_fase()
            self.score.prep_naves()
            self.jogo_ativo = True

            # Limpa os aliens e misseis que restarem
            self.missel.empty()
            self.alien.empty()

            # Cria uma nova frota e reposiciona a nave
            self._criar_frota()
            self.nave.centraliza_nave()

            # Esconde o cursor do mouse
            pygame.mouse.set_visible(False)


    def _checar_teclaspress_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = True
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._disparar_missel()       

    def _checar_soltarteclas_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = False
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = False
    
    def _disparar_missel(self):
        if len(self.missel) < self.settings.disparos_por_vez:
            novo_missel = Missel(self)
            self.missel.add(novo_missel)

    def _atualiza_missel(self):
        """Atualiza a posição dos mísseis e remove os que saíram da tela."""
        self.missel.update()

        # Remove mísseis que ultrapassaram o limite superior da tela.
        for missel in self.missel.copy():
            if missel.rect.bottom <= 0:
                self.missel.remove(missel)

        self._checar_misseis_colididos()
        

    def _checar_misseis_colididos(self):

        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        colisao = pygame.sprite.groupcollide(
                self.missel, self.alien, True, True)

        if colisao:
            for alien in colisao.values():
                self.estatisticas.score += self.settings.pontos_alien * len(alien)
            self.score.prep_score()
            self.score.checa_pontuacao_maxima()

        if not self.alien:
            # Destroy existing bullets and create new fleet.
            self.missel.empty()
            self._criar_frota()
            self.settings.aumentar_velocidade()

            # Increase level.
            self.estatisticas.level += 1
            self.score.prep_fase()           
        
    
    def _atualiza_aliens(self):
        self._checar_frota_borda()
        self.alien.update()

        if pygame.sprite.spritecollideany(self.nave, self.alien):
            self._batidas_nave()

        self._checar_alien_final_tela()

    def _batidas_nave(self):
        if self.estatisticas.naves_restantes> 0:
            #reduz uma vida
            self.estatisticas.naves_restantes-=1
            self.score.prep_naves()

            #descarta os misseis e naves que restarem
            self.missel.empty()
            self.alien.empty()

            #reinicia o jogo com a nave no centro
            self._criar_frota()
            self.nave.centraliza_nave()

            #faz uma pausa
            sleep(0.5)    
        else:
            self.jogo_ativo = False
            pygame.mouse.set_visible(True)
        
    def _checar_alien_final_tela(self):
        for alien in self.alien.sprites():
            if alien.rect.bottom >= self.settings.altura_tela:
                self._batidas_nave()  # Tratar como se a nave fosse abatida
                break


    def _criar_frota(self):
        alien = Alien(self)
        self.alien.add(alien)
        alien_largura, alien_altura= alien.rect.size

        current_x, current_y = alien_largura, alien_altura
        while current_y < (self.settings.altura_tela - 3 * alien_altura):
            while current_x < (self.settings.largura_tela- 2 * alien_largura):
                self._criar_alien(current_x, current_y)
                current_x += 2 * alien_largura

            current_x = alien_largura
            current_y += 2 * alien_altura

    def _criar_alien(self, x_position, y_position):
            novo_alien = Alien(self)
            novo_alien.x = x_position
            novo_alien.rect.x = x_position
            novo_alien.rect.y = y_position
            self.alien.add(novo_alien)

    def _checar_frota_borda(self):
        for alien in self.alien.sprites():
            if alien.checar_borda():
                self._muda_direcao_frota()
                break

    def _muda_direcao_frota(self):
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.velocidade_frota
        self.settings.direcao_frota *= -1

    def _atualiza_tela(self):
        """Atualiza as imagens na tela e alterna para a nova tela."""
        # Preenche a tela com a cor de fundo.
        self.screen.fill(self.settings.bg_color)

        # Desenha todos os mísseis na tela.
        for missel in self.missel.sprites():
            missel.gerar_missel()
        self.nave.blitme()
        self.alien.draw(self.screen)

        # Mostra as informações de pontuação
        self.score.mostra_score()

        # Desenha o botao na tela se o jogo estiver inativo
        if not self.jogo_ativo:
            self.botao_play.desenha_botao()

        # Atualiza a tela.
        pygame.display.flip()

if __name__ == '__main__':
    ia = InvasaoAlienigena()
    ia.jogo_on()
