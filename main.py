import pygame
import sys
from button import ImageButton
import game

pygame.init()
W, H = 1920, 980
menu_background = pygame.image.load('images/background_menu.jpg')
pygame.mixer.music.load('sounds/menu_music.mp3')
pygame.mixer.music.play(-1)
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60


def main_second_start():
    pygame.mixer.music.load('sounds/menu_music.mp3')
    pygame.mixer.music.play(-1)
    main_menu()


def main_menu():
    pygame.display.set_caption('Catch a coin|Menu')
    start_but = ImageButton(W / 2 - (300 / 2), 350, 300, 150, '', 'images/start1.png', 'images/start2.png',
                            'sounds/menu_click.mp3')
    settings_but = ImageButton(W / 2 - (300 / 2), 500, 300, 150, 'Настройки', 'images/title1.png', 'images/title2.png',
                               'sounds/menu_click.mp3')
    exit_but = ImageButton(W / 2 - (300 / 2), 650, 300, 150, 'Выход', 'images/exit1.png', 'images/exit2.png',
                           'sounds/menu_click.mp3')

    running = True
    while running:
        sc.fill((0, 0, 0))
        sc.blit(menu_background, (0, 0))

        font = pygame.font.SysFont('Arial Black', 72)
        text_surface = font.render('CATCH A COIN', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(W / 2, 100))
        sc.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            try:
                if event.type == pygame.USEREVENT:
                    if event.button == start_but:
                        game.start()

                if event.type == pygame.USEREVENT and event.button == settings_but:
                    settings_menu()

                if event.type == pygame.USEREVENT and event.button == exit_but:
                    sys.exit(0)

            except AttributeError:
                continue

            for btn in [start_but, settings_but, exit_but]:
                btn.handle_event(event)

        for btn in [start_but, settings_but, exit_but]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(sc)

        pygame.display.flip()


def settings_menu():
    audio_button = ImageButton(W / 2 - (300 / 2), (H / 2), 300, 150, '', 'images/sound_but_on.png',
                               'images/sound_but_off.png', 'sounds/menu_click.mp3')
    back_button = ImageButton(W / 2 - (100 / 2), 800, 100, 100, '<-', 'images/back_btn1.png', 'images/back_btn2.png',
                              'sounds/menu_click.mp3')

    running = True
    while running:
        sc.fill((0, 0, 0))
        sc.blit(menu_background, (0, 0))

        font = pygame.font.SysFont('Arial Black', 72)
        text_surface = font.render('Settings (в разработке)', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(W / 2, 100))
        sc.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            try:
                if event.type == pygame.USEREVENT:
                    if event.button == audio_button:
                        pass

                    if event.button == back_button:
                        main_menu()

            except AttributeError:
                continue

            for btn in [audio_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(sc)

        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
