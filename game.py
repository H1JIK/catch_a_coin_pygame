import pygame
from random import randint
from button import ImageButton
import sys
import main

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

s_catch = pygame.mixer.Sound('sounds/catch.mp3')

BLACK = (0, 0, 0)
W, H = 1920, 980

sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()


def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            s_catch.play()
            game_score += ball.score
            ball.kill()


def createBall(group):
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)


score = pygame.image.load('images/score_fon.png').convert_alpha()
f = pygame.font.SysFont('arial black', 20)

telega = pygame.image.load('images/telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=W // 2, bottom=H - 5)

balls_data = ({'path': 'bronze_coin.png', 'score': 100},
              {'path': 'silver_coin.png', 'score': 150},
              {'path': 'gold_coin.png', 'score': 200})

balls_surf = [pygame.image.load('images/' + data['path']).convert_alpha() for data in balls_data]

game_score = 0

balls = pygame.sprite.Group()

bg = pygame.image.load('images/background.png').convert()

speed = 10
createBall(balls)

def start():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.music.load('sounds/music_fon.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, 2000)

    pygame.mixer.music.load('sounds/music_fon.mp3')
    pygame.mixer.music.play(-1)
    pause_button = ImageButton(1820, 25, 75, 75, '', 'images/pause1.png',
                               'images/pause2.png', 'sounds/menu_click.mp3')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                createBall(balls)

            try:
                if event.type == pygame.USEREVENT:
                    if event.button == pause_button:
                        # from main import main_second_start
                        main.main_second_start()
            except AttributeError:
                continue

            for btn in [pause_button]:
                btn.handle_event(event)

        for btn in [pause_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(sc)

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            t_rect.x -= speed
            if t_rect.x < 0:
                t_rect.x = 0
        elif keys[pygame.K_RIGHT]:
            t_rect.x += speed
            if t_rect.x > W - t_rect.width:
                t_rect.x = W - t_rect.width

        collideBalls()

        sc.blit(bg, (0, 0))
        sc.blit(score, (0, -65))
        sc_text = f.render(f'Счет: {str(game_score)}', 1, (94, 138, 14))
        sc.blit(sc_text, (35, 20))

        balls.draw(sc)
        sc.blit(telega, t_rect)
        pygame.display.update()
        pygame.display.set_caption(f'Catch a coin|Score: {game_score}')



        clock.tick(FPS)

        balls.update(H)