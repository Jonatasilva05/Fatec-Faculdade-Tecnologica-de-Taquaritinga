import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Futebol GOL A GOL")

WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("arial", 45)

IMG = "img"
JOGADOR_IMG_ORIGINAL = pygame.image.load(os.path.join(IMG, "amarelo.png"))
RIVAL_IMG = pygame.image.load(os.path.join(IMG, "azul.png"))
BOLA_IMG = pygame.image.load(os.path.join(IMG, "bola.png"))
CAMPO_IMG_FASE1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG, "campo.png")), (WIDTH, HEIGHT))
CAMPO_IMG_FASE2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG, "terra.png")), (WIDTH, HEIGHT))

RIVAL_IMG = pygame.transform.scale(RIVAL_IMG, (80, 100))
BOLA_IMG = pygame.transform.scale(BOLA_IMG, (30, 30))

clock = pygame.time.Clock()

def draw_window(player, player_img, rival, ball, placar, placar_rival, fase, campo_img):
    WIN.blit(campo_img, (0, 0))
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
    player_img = pygame.transform.scale(JOGADOR_IMG_ORIGINAL, (player_width * 2, player_height * 2))

    player_speed = 5
    rival = pygame.Rect(WIDTH - 140, HEIGHT//2, 40, 60)
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, 30, 30)
    ball_vel = [5, 0]

    placar = 0
    placar_rival = 0
    run = True
    tempo_ultimo_aumento = pygame.time.get_ticks()
    campo_atual = CAMPO_IMG_FASE1

    def reset_positions():
        nonlocal player_width, player_height, player_speed, player_img, tempo_ultimo_aumento
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
        tempo_ultimo_aumento = pygame.time.get_ticks()

    while run:
        clock.tick(60 + (fase - 1) * 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_ultimo_aumento >= 3000:
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            if player_width - 2 >= 30:
                player_width -= 2
            if player_height - 2 >= 50:
                player_height -= 2
            player_speed += 0.3
            center = player.center
            player.width = player_width
            player.height = player_height
            player.center = center
            player_img = pygame.transform.scale(JOGADOR_IMG_ORIGINAL, (player_width * 2, player_height * 2))
            tempo_ultimo_aumento = tempo_atual

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= int(player_speed)
        if keys[pygame.K_DOWN] and player.y + player.height < HEIGHT:
            player.y += int(player_speed)

        if rival.centery < ball.centery:
            rival.y += 3 + fase
        elif rival.centery > ball.centery:
            rival.y -= 3 + fase

        ball.x += int(ball_vel[0])
        ball.y += int(ball_vel[1])

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel[1] *= -1

        if player.colliderect(ball):
            ball_vel[0] = abs(ball_vel[0])
            ball_vel[1] = random.randint(-5, 5)

        if rival.colliderect(ball):
            ball_vel[0] = -abs(ball_vel[0])
            ball_vel[1] = random.randint(-5, 5)

        
        if ball.left <= 10:
            if HEIGHT//2 - 50 < ball.centery < HEIGHT//2 + 50:
                if fase == 2:
                    placar += 1  
                else:
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

        
        if ball.right >= WIDTH - 10:
            if HEIGHT//2 - 50 < ball.centery < HEIGHT//2 + 50:
                if fase == 2:
                    placar_rival += 1  
                else:
                    placar += 1
                reset_positions()
                ball_vel[0] *= 1.2
                ball_vel[1] *= 1.2
            else:
                ball.right = WIDTH - 10
                ball_vel[0] *= -1

        draw_window(player, player_img, rival, ball, placar, placar_rival, fase, campo_atual)

        if placar >= 1 and fase == 1:
            fase = 2
            campo_atual = CAMPO_IMG_FASE2
            placar = 0
            placar_rival = 0
            reset_positions()

        if fase == 2 and placar >= 3:
            WIN.fill((0, 0, 0))
            win_text = FONT.render("Parabéns! Venceu a Fase 2!", True, WHITE)
            WIN.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
