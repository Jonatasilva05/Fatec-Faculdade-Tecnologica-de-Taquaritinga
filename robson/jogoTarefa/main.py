import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Futebol GOL A GOL")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
FONT = pygame.font.SysFont("arial", 45)

IMG = "img"
JOGADOR_IMG_ORIGINAL = pygame.image.load(os.path.join(IMG, "amarelo.png"))
RIVAL_IMG = pygame.image.load(os.path.join(IMG, "azul.png"))
BOLA_IMG = pygame.image.load(os.path.join(IMG, "bola.png"))
CAMPO_IMG = pygame.image.load(os.path.join(IMG, "campo.png"))
CAMPO_IMG = pygame.transform.scale(CAMPO_IMG, (WIDTH, HEIGHT))

RIVAL_IMG = pygame.transform.scale(RIVAL_IMG, (80, 100))
BOLA_IMG = pygame.transform.scale(BOLA_IMG, (30, 30))

clock = pygame.time.Clock()

def draw_window(player, player_img, rival, ball, placar, placar_rival, fase):
    WIN.blit(CAMPO_IMG, (0, 0))
    pygame.draw.rect(WIN, WHITE, (WIDTH//2 - 2, 0, 4, HEIGHT))
    pygame.draw.rect(WIN, WHITE, (0, HEIGHT//2 - 50, 10, 100))  
    pygame.draw.rect(WIN, WHITE, (WIDTH - 10, HEIGHT//2 - 50, 10, 100))  

    WIN.blit(player_img, (player.x, player.y))
    WIN.blit(RIVAL_IMG, (rival.x, rival.y))
    WIN.blit(BOLA_IMG, (ball.x, ball.y))

    texto = FONT.render(f"Você {placar} x {placar_rival} IA | Fase {fase}", True, WHITE)
    WIN.blit(texto, (WIDTH//2 - texto.get_width()//2, 10))

    pygame.display.update()

def main():
    fase = 1
    player_width, player_height = 40, 60
    player = pygame.Rect(100, HEIGHT//2, player_width, player_height)
    player_img = pygame.transform.scale(JOGADOR_IMG_ORIGINAL, (player_width * 2, player_height * 2))  # *2 pq imagem > hitbox

    player_speed = 5
    rival = pygame.Rect(WIDTH - 140, HEIGHT//2, 40, 60)
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, 30, 30)
    ball_vel = [random.choice([-5, 5]), random.choice([-3, 3])]

    placar = 0
    placar_rival = 0
    run = True
    tempo_ultimo_aumento = pygame.time.get_ticks()

    def reset_positions():
        nonlocal player_width, player_height, player_speed, player_img
        player.y = HEIGHT // 2
        rival.y = HEIGHT // 2
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_vel[0] = random.choice([-5, 5])
        ball_vel[1] = random.choice([-3, 3])
        player_width, player_height = 40, 60
        player_speed = 5
        player.width = player_width
        player.height = player_height
        player_img = pygame.transform.scale(JOGADOR_IMG_ORIGINAL, (player_width * 2, player_height * 2))
        nonlocal tempo_ultimo_aumento
        tempo_ultimo_aumento = pygame.time.get_ticks()

    while run:
        clock.tick(60 + (fase - 1) * 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # ⏱ Aumento gradual da velocidade da bola + redução do jogador
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_ultimo_aumento >= 3000:
            # Aumenta velocidade da bola
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1

            if player_width - 2 >= 10:
                player_width -= 2
            if player_height - 2 >= 30:
                player_height -= 2


            # Aumenta velocidade do jogador
            player_speed += 0.3

            # Recalcula posição para manter o centro
            center = player.center
            player.width = player_width
            player.height = player_height
            player.center = center

            # Redimensiona imagem
            player_img = pygame.transform.scale(JOGADOR_IMG_ORIGINAL, (player_width * 2, player_height * 2))

            tempo_ultimo_aumento = tempo_atual

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= int(player_speed)
        if keys[pygame.K_DOWN] and player.y + player.height < HEIGHT:
            player.y += int(player_speed)

        # IA
        if rival.centery < ball.centery:
            rival.y += 3 + fase
        elif rival.centery > ball.centery:
            rival.y -= 3 + fase

        # Movimento da bola
        ball.x += int(ball_vel[0])
        ball.y += int(ball_vel[1])

        # Rebote
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel[1] *= -1

        # Colisão com jogador
        if player.colliderect(ball):
            ball_vel[0] = abs(ball_vel[0])
            ball_vel[1] = random.randint(-5, 5)

        # Colisão com rival
        if rival.colliderect(ball):
            ball_vel[0] = -abs(ball_vel[0])
            ball_vel[1] = random.randint(-5, 5)

        # Gol do rival
        if ball.left <= 10:
            if HEIGHT//2 - 50 < ball.centery < HEIGHT//2 + 50:
                placar_rival += 1
                reset_positions()

                if placar_rival >= 10:
                    WIN.fill((0, 0, 0))
                    game_over = FONT.render("Game Over! A IA venceu!", True, WHITE)
                    WIN.blit(game_over, (WIDTH//2 - game_over.get_width()//2, HEIGHT//2))
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    continue
            else:
                ball.left = 10
                ball_vel[0] *= -1

        # Gol do jogador
        if ball.right >= WIDTH - 10:
            if HEIGHT//2 - 50 < ball.centery < HEIGHT//2 + 50:
                placar += 1
                reset_positions()
                ball_vel[0] *= 1.2
                ball_vel[1] *= 1.2
            else:
                ball.right = WIDTH - 10
                ball_vel[0] *= -1

        draw_window(player, player_img, rival, ball, placar, placar_rival, fase)

        if placar >= 3:
            fase += 1
            placar = 0
            placar_rival = 0
            reset_positions()
            if fase > 2:
                WIN.fill((0, 0, 0))
                win_text = FONT.render("Parabéns! Venceu 2 partidas!", True, WHITE)
                WIN.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2))
                pygame.display.update()
                pygame.time.delay(4000)
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
