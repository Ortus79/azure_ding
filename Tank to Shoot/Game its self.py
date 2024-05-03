# --------------------------------------------------------------------------------------------------------------------------------------
# Autor :   Nico Scherer
# Project:  Tank2Shoot game
# --------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------------------------------------------
import pygame
import random
import os.path
import threading

# --------------------------------------------------------------------------------------------------------------------------------------
pygame.init()
pygame.font.init()


# --------------------------------------------------------------------------------------------------------------------------------------
# Color
# --------------------------------------------------------------------------------------------------------------------------------------
black = 0,0,0

# --------------------------------------------------------------------------------------------------------------------------------------
# Screen
# --------------------------------------------------------------------------------------------------------------------------------------
screen_top = pygame.Rect(0,0,900,0)
screen_bottom = pygame.Rect(0,500,900,0)
screen_left = pygame.Rect(0,0,0,500)
screen_right = pygame.Rect(900,0,0,500)

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank2Shoot")


# --------------------------------------------------------------------------------------------------------------------------------------
# Bilder pro Sekunden
# --------------------------------------------------------------------------------------------------------------------------------------
FPS = 60

# --------------------------------------------------------------------------------------------------------------------------------------
# language
# --------------------------------------------------------------------------------------------------------------------------------------
language_f = "English"
# --------------------------------------------------------------------------------------------------------------------------------------
# basic stuf
# --------------------------------------------------------------------------------------------------------------------------------------
resourcpack_folder = "Textures"

TANKS_WIDTH, TANKS_HEIGHT = 40, 45
def load_stuf():
    global textures, Red_tank, Blue_tank, text_surface

    textures = [
        pygame.image.load(os.path.join(f"{resourcpack_folder}\HomeScreen.png")),                # 0
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Tank_red.png")),                  # 1
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Tank_blue.png")),                 # 2
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Eastereg.png")),                  # 3
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Button_422x50px.png")),           # 4
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Button_422x50px_pressed.png")),   # 5
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Escape_Menu.png")),               # 6
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Button_200x50px.png")),           # 7
        pygame.image.load(os.path.join(f"{resourcpack_folder}\Button_200x50px_pressed.png"))    # 8
    ]

    Red_tank = pygame.transform.scale(textures[1], (TANKS_WIDTH, TANKS_HEIGHT))
    Blue_tank = pygame.transform.rotate(pygame.transform.scale(textures[2], (TANKS_WIDTH, TANKS_HEIGHT)), 180)

    language_file = open(f"Languages\{language_f}")
    language_text = language_file.read()
    language_file.close()
    language_text_list = language_text.split(",")

    resume_text = language_text_list[0]
    main_menu_text = language_text_list[1]
    quit_game_text = language_text_list[2]
    options_text = language_text_list[3]
    recourcpack_text = language_text_list[4]
    play_text = language_text_list[5]
    back_text = language_text_list[6]
    apply_text = language_text_list[7]
    volume_text = language_text_list[8]
    language_settng_text = language_text_list[9]
    keybinds_text = language_text_list[10]

    my_font = pygame.font.SysFont("impact",25)

    text_surface = [
        my_font.render(resume_text, False, (0, 0, 0)),              # 0
        my_font.render(main_menu_text, False, (0, 0, 0)),           # 1
        my_font.render(quit_game_text, False, (0, 0, 0)),           # 2
        my_font.render(options_text, False, (0, 0, 0)),             # 3
        my_font.render(recourcpack_text, False, (0, 0, 0)),         # 4
        my_font.render(play_text, False, (0, 0, 0)),                # 5
        my_font.render(back_text, False, (0, 0, 0)),                # 6
        my_font.render(apply_text, False, (0, 0, 0)),               # 7
        my_font.render(volume_text, False, (0, 0, 0)),              # 8
        my_font.render(language_settng_text, False, (0, 0, 0)),     # 9
        my_font.render(keybinds_text, False, (0, 0, 0))             # 10
    ]


x_speed_red = 0
y_speed_red = 0

x_speed_blue = 0
y_speed_blue = 0

bullet_speed = 5
bullet_width = 5
bullet_height = 10
bullet_color = (0, 0, 0)  # Red color for the red tank's bullets

# --------------------------------------------------------------------------------------------------------------------------------------
# Maps
# --------------------------------------------------------------------------------------------------------------------------------------
map1_rects = [
pygame.Rect(200, 100, 10, 200),
pygame.Rect(420, 150, 10, 250),
pygame.Rect(380, 210, 200, 10),
pygame.Rect(300, 400, 434, 10),
pygame.Rect(95, 300, 10, 200),
pygame.Rect(120, 100, 200, 10),
pygame.Rect(570, 100, 10, 200),
pygame.Rect(650, 100, 200, 10),
pygame.Rect(750, 100, 10, 230)
]
map2_rects = [
pygame.Rect(200, 50, 200, 10),
pygame.Rect(430, 170, 250, 10),
pygame.Rect(480, 240, 10, 200),
pygame.Rect(300, 390, 10, 434),
pygame.Rect(95, 300, 200, 10),
pygame.Rect(120, 40, 10, 200),
pygame.Rect(630, 80, 10, 200),
pygame.Rect(760, 110, 230, 10)
]
map3_rects = [
pygame.Rect(700, 235, 10, 200),
pygame.Rect(380, 150, 10, 300),
pygame.Rect(470, 40, 180, 10),
pygame.Rect(240, 370, 10, 200),
pygame.Rect(100, 250, 230, 10),
pygame.Rect(500, 215, 170, 10),
pygame.Rect(680, 135, 100, 10),
pygame.Rect(300, 50, 10, 120)
]
map4_rects = [
pygame.Rect(700, 235, 200, 10),
pygame.Rect(380, 150, 300, 10),
pygame.Rect(480, 60, 10, 180),
pygame.Rect(240, 370, 200, 10),
pygame.Rect(100, 250, 10, 230),
pygame.Rect(590, 215, 10, 170),
pygame.Rect(200, 135, 10, 100),
pygame.Rect(300, 50, 120, 10)
]
map5_rects = [
pygame.Rect(540, 350, 305, 10),
pygame.Rect(400, 150, 10, 290),
pygame.Rect(180, 80, 420, 10),
pygame.Rect(100, 140, 10, 340),
pygame.Rect(160, 240, 150, 10),
pygame.Rect(670, 140, 10, 170)
]

# --------------------------------------------------------------------------------------------------------------------------------------
# Maps Zeichnen
# --------------------------------------------------------------------------------------------------------------------------------------
def Map_1():
    for i in range(len(map1_rects)):
        pygame.draw.rect(SCREEN, (0, 0, 0), map1_rects[i])
def Map_2():
    for i in range(len(map2_rects)):
        pygame.draw.rect(SCREEN, (0, 0, 0), map2_rects[i])
def Map_3():
    for i in range(len(map3_rects)):
        pygame.draw.rect(SCREEN, (0, 0, 0), map3_rects[i])
def Map_4():
    for i in range(len(map4_rects)):
        pygame.draw.rect(SCREEN, (0, 0, 0), map4_rects[i])
def Map_5():
    for i in range(len(map5_rects)):
        pygame.draw.rect(SCREEN, (0, 0, 0), map5_rects[i])


Maps = [Map_1, Map_2, Map_3, Map_4, Map_5]

mn = random.randint(0, 4)

k = Maps[mn]

map_lists = [map1_rects, map2_rects, map3_rects, map4_rects, map5_rects]

# --------------------------------------------------------------------------------------------------------------------------------------
# Colisions
# --------------------------------------------------------------------------------------------------------------------------------------
def map_1_colisions_blue(blue):
    global x_speed_blue, y_speed_blue
    for wall in map1_rects:
        if wall.colliderect(blue.x + x_speed_blue, blue.y, blue.width, blue.height):
            x_speed_blue = 0

        if wall.colliderect(blue.x, blue.y + y_speed_blue, blue.width, blue.height):
            if y_speed_blue < 0:
                y_speed_blue = wall.bottom - blue.top
            else:
                y_speed_blue = wall.top - blue.bottom
def map_1_colisions_red(red):
    global x_speed_red, y_speed_red
    for wall in map1_rects:
        if wall.colliderect(red.x + x_speed_red, red.y, red.width, red.height):
            x_speed_red = 0

        if wall.colliderect(red.x, red.y + y_speed_red, red.width, red.height):
            if y_speed_red < 0:
                y_speed_red = wall.bottom - red.top
            else:
                y_speed_red = wall.top - red.bottom

def map_2_colisions_blue(blue):
    global x_speed_blue, y_speed_blue
    for wall in map2_rects:
        if wall.colliderect(blue.x + x_speed_blue, blue.y, blue.width, blue.height):
            x_speed_blue = 0

        if wall.colliderect(blue.x, blue.y + y_speed_blue, blue.width, blue.height):
            if y_speed_blue < 0:
                y_speed_blue = wall.bottom - blue.top
            else:
                y_speed_blue = wall.top - blue.bottom
def map_2_colisions_red(red):
    global x_speed_red, y_speed_red
    for wall in map2_rects:
        if wall.colliderect(red.x + x_speed_red, red.y, red.width, red.height):
            x_speed_red = 0

        if wall.colliderect(red.x, red.y + y_speed_red, red.width, red.height):
            if y_speed_red < 0:
                y_speed_red = wall.bottom - red.top
            else:
                y_speed_red = wall.top - red.bottom

def map_3_colisions_blue(blue):
    global x_speed_blue, y_speed_blue
    for wall in map3_rects:
        if wall.colliderect(blue.x + x_speed_blue, blue.y, blue.width, blue.height):
            x_speed_blue = 0

        if wall.colliderect(blue.x, blue.y + y_speed_blue, blue.width, blue.height):
            if y_speed_blue < 0:
                y_speed_blue = wall.bottom - blue.top
            else:
                y_speed_blue = wall.top - blue.bottom
def map_3_colisions_red(red):
    global x_speed_red, y_speed_red
    for wall in map3_rects:
        if wall.colliderect(red.x + x_speed_red, red.y, red.width, red.height):
            x_speed_red = 0

        if wall.colliderect(red.x, red.y + y_speed_red, red.width, red.height):
            if y_speed_red < 0:
                y_speed_red = wall.bottom - red.top
            else:
                y_speed_red = wall.top - red.bottom

def map_4_colisions_blue(blue):
    global x_speed_blue, y_speed_blue
    for wall in map4_rects:
        if wall.colliderect(blue.x + x_speed_blue, blue.y, blue.width, blue.height):
            x_speed_blue = 0

        if wall.colliderect(blue.x, blue.y + y_speed_blue, blue.width, blue.height):
            if y_speed_blue < 0:
                y_speed_blue = wall.bottom - blue.top
            else:
                y_speed_blue = wall.top - blue.bottom
def map_4_colisions_red(red):
    global x_speed_red, y_speed_red
    for wall in map4_rects:
        if wall.colliderect(red.x + x_speed_red, red.y, red.width, red.height):
            x_speed_red = 0

        if wall.colliderect(red.x, red.y + y_speed_red, red.width, red.height):
            if y_speed_red < 0:
                y_speed_red = wall.bottom - red.top
            else:
                y_speed_red = wall.top - red.bottom

def map_5_colisions_blue(blue):
    global x_speed_blue, y_speed_blue
    for wall in map5_rects:
        if wall.colliderect(blue.x + x_speed_blue, blue.y, blue.width, blue.height):
            x_speed_blue = 0

        if wall.colliderect(blue.x, blue.y + y_speed_blue, blue.width, blue.height):
            if y_speed_blue < 0:
                y_speed_blue = wall.bottom - blue.top
            else:
                y_speed_blue = wall.top - blue.bottom
def map_5_colisions_red(red):
    global x_speed_red, y_speed_red
    for wall in map5_rects:
        if wall.colliderect(red.x + x_speed_red, red.y, red.width, red.height):
            x_speed_red = 0

        if wall.colliderect(red.x, red.y + y_speed_red, red.width, red.height):
            if y_speed_red < 0:
                y_speed_red = wall.bottom - red.top
            else:
                y_speed_red = wall.top - red.bottom

def collision_screenborder(red, blue):
    if red.left <= 0:
        red.left = screen_left.right

    if red.top <= 0:
        red.top = screen_top.bottom

    if red.right >= SCREEN_WIDTH:
        red.right = screen_right.left

    if red.bottom >= SCREEN_HEIGHT:
        red.bottom = screen_bottom.top

    if blue.left <= 0:
        blue.left = screen_left.right

    if blue.top <= 0:
        blue.top = screen_top.bottom

    if blue.right >= SCREEN_WIDTH:
        blue.right = screen_right.left

    if blue.bottom >= SCREEN_HEIGHT :
        blue.bottom = screen_bottom.top


# --------------------------------------------------------------------------------------------------------------------------------------
# Objekte Zeichnen
# --------------------------------------------------------------------------------------------------------------------------------------
def draw_window(red, blue):
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(Blue_tank, (blue.x, blue.y))
    SCREEN.blit(Red_tank, (red.x, red.y))
    k()
    collision_screenborder(red, blue)


# --------------------------------------------------------------------------------------------------------------------------------------
# Bewegung von Panzer
# --------------------------------------------------------------------------------------------------------------------------------------
def rotation_red(key_hit, Red_tank_image, TANKS_WIDTH, TANKS_HEIGHT):
    global Red_tank
    if key_hit[pygame.K_w] == True:
        Red_tank = pygame.transform.rotate(pygame.transform.scale(Red_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 180)

    elif key_hit[pygame.K_s] == True:
        Red_tank = pygame.transform.rotate(pygame.transform.scale(Red_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 0)

    elif key_hit[pygame.K_a] == True:
        Red_tank = pygame.transform.rotate(pygame.transform.scale(Red_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 270)

    elif key_hit[pygame.K_d] == True:
        Red_tank = pygame.transform.rotate(pygame.transform.scale(Red_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 90)
def rotation_blue(key_hit, Blue_tank_image, TANKS_WIDTH, TANKS_HEIGHT):
    global Blue_tank
    if key_hit[pygame.K_UP] == True:
        Blue_tank = pygame.transform.rotate(pygame.transform.scale(Blue_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 180)

    elif key_hit[pygame.K_DOWN] == True:
        Blue_tank = pygame.transform.rotate(pygame.transform.scale(Blue_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 0)

    elif key_hit[pygame.K_LEFT] == True:
        Blue_tank = pygame.transform.rotate(pygame.transform.scale(Blue_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 270)

    elif key_hit[pygame.K_RIGHT] == True:
        Blue_tank = pygame.transform.rotate(pygame.transform.scale(Blue_tank_image, (TANKS_WIDTH, TANKS_HEIGHT)), 90)

def speed_red(key):
    global y_speed_red, x_speed_red

    if key[pygame.K_w] == True:
        y_speed_red = -2
    elif key[pygame.K_s] == True:
        y_speed_red = 2

    elif key[pygame.K_a] == True:
        x_speed_red = -2

    elif key[pygame.K_d] == True:
        x_speed_red = 2
def speed_blue(key):
    global y_speed_blue, x_speed_blue
    if key[pygame.K_UP] == True:
        y_speed_blue = -2

    elif key[pygame.K_DOWN] == True:
        y_speed_blue = 2

    elif key[pygame.K_LEFT] == True:
        x_speed_blue = - 2

    elif key[pygame.K_RIGHT] == True:
        x_speed_blue = 2

def Move_red(red, key):
    global x_speed_red
    global y_speed_red
    if key[pygame.K_w] == True:
        red.y += y_speed_red

    elif key[pygame.K_s] == True:
        red.y += y_speed_red

    elif key[pygame.K_a] == True:
        red.x += x_speed_red

    elif key[pygame.K_d] == True:
        red.x += x_speed_red
def Move_blue(blue, key):
    global x_speed_blue
    global y_speed_blue
    if key[pygame.K_UP] == True:
        blue.y += y_speed_blue

    elif key[pygame.K_DOWN] == True:
        blue.y += y_speed_blue

    elif key[pygame.K_LEFT] == True:
        blue.x += x_speed_blue

    elif key[pygame.K_RIGHT] == True:
        blue.x += x_speed_blue

# --------------------------------------------------------------------------------------------------------------------------------------
# bullets
# --------------------------------------------------------------------------------------------------------------------------------------
def shoot_red(red):
    bullet_rect = pygame.Rect(red.x + red.width // 2 - bullet_width // 2, red.y + red.height, bullet_width, bullet_height)

    bullet_rect.y -= bullet_speed

    pygame.draw.rect(SCREEN, bullet_color, bullet_rect)

def shoot_blue(blue):
    bullet_rect = pygame.Rect(blue.x + blue.width // 2 - bullet_width // 2, blue.y, bullet_width, bullet_height)

    bullet_rect.y += bullet_speed

    pygame.draw.rect(SCREEN, bullet_color, bullet_rect)

# --------------------------------------------------------------------------------------------------------------------------------------
# language
# --------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------
# ESC Menü
# --------------------------------------------------------------------------------------------------------------------------------------
def esc_menue(red,blue):
    esc = True
    clock = pygame.time.Clock()
    SCREEN.blit(textures[6], (0, 0))

    SCREEN.blit(textures[4], (239, 230))
    resume_button = pygame.Rect(239, 230, 422, 50)
    SCREEN.blit(text_surface[0],text_surface[0].get_rect(center=resume_button.center))

    SCREEN.blit(textures[4], (239, 290))
    options_button = pygame.Rect(239, 290, 422, 50)
    SCREEN.blit(text_surface[3], text_surface[3].get_rect(center=options_button.center))

    SCREEN.blit(textures[4], (239, 350))
    main_menu_button = pygame.Rect(239, 350, 422, 50)
    SCREEN.blit(text_surface[1], text_surface[1].get_rect(center=main_menu_button.center))

    while esc:
        clock.tick(FPS)

        pos_mous = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if options_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 290))
                        SCREEN.blit(text_surface[3], text_surface[3].get_rect(center=options_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 290))
                        SCREEN.blit(text_surface[3], text_surface[3].get_rect(center=options_button.center))
                        options_esc(red, blue)
                        esc = False

            if resume_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 230))
                        SCREEN.blit(text_surface[0], text_surface[0].get_rect(center=resume_button.center))
                        pygame.display.update()

                        esc = False
                        SCREEN.blit(textures[4], (239, 230))
                        SCREEN.blit(text_surface[1], text_surface[1].get_rect(center=resume_button.center))
                        run_game(red, blue)

            if main_menu_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 350))
                        SCREEN.blit(text_surface[1], text_surface[1].get_rect(center=main_menu_button.center))
                        pygame.display.update()

                        esc = False
                        SCREEN.blit(textures[4], (239, 350))
                        SCREEN.blit(text_surface[1], text_surface[1].get_rect(center=main_menu_button.center))
                        Game_While_Running()


            if event.type == pygame.QUIT:
                esc = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_game(red,blue)
                    esc = False
        pygame.display.update()
    pygame.quit()
# --------------------------------------------------------------------------------------------------------------------------------------
# Running game
# --------------------------------------------------------------------------------------------------------------------------------------
def run_game(red,blue):
    playing = True
    clock = pygame.time.Clock()
    while playing:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        speed_red(key)
        speed_blue(key)

        if mn == 0:
            map_1_colisions_blue(blue)
            map_1_colisions_red(red)
        elif mn == 1:
            map_2_colisions_blue(blue)
            map_2_colisions_red(red)
        elif mn == 2:
            map_3_colisions_blue(blue)
            map_3_colisions_red(red)
        elif mn == 3:
            map_4_colisions_blue(blue)
            map_4_colisions_red(red)
        elif mn == 4:
            map_5_colisions_blue(blue)
            map_5_colisions_red(red)

        shoot_red(red)
        shoot_blue(blue)

        Move_red(red, key)
        Move_blue(blue, key)

        rotation_red(key, textures[1], TANKS_WIDTH, TANKS_HEIGHT)
        rotation_blue(key, textures[2], TANKS_WIDTH, TANKS_HEIGHT)

        draw_window(red, blue)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    esc_menue(red,blue)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # For example, press space to shoot
                    x = threading.Thread(target=shoot_blue(blue))
                    x.start()
                elif event.key == pygame.K_RETURN:  # For example, press enter to shoot for blue tank
                    x = threading.Thread(target=shoot_red(red))
                    x.start()
        pygame.display.update()
    pygame.quit()
def Game_While_Running():
    RUN = True

    red = pygame.Rect((50, 50, 40, 40))
    blue = pygame.Rect((800, 400, 40, 40))

    clock = pygame.time.Clock()
    SCREEN.blit(textures[0], (0, 0))

    SCREEN.blit(textures[4], (239,200))
    play_button = pygame.Rect(239, 200, 422, 50)
    SCREEN.blit(text_surface[5], text_surface[5].get_rect(center=play_button.center))

    SCREEN.blit(textures[4], (239,260))
    options_button = pygame.Rect(239, 260, 422, 50)
    SCREEN.blit(text_surface[3], text_surface[3].get_rect(center=options_button.center))

    SCREEN.blit(textures[4], (239, 320))
    recourcpack_button = pygame.Rect(239, 320, 422, 50)
    SCREEN.blit(text_surface[4], text_surface[4].get_rect(center=recourcpack_button.center))

    SCREEN.blit(textures[4], (239,380))
    quit_game_button = pygame.Rect(239, 380, 422, 50)
    SCREEN.blit(text_surface[2], text_surface[2].get_rect(center=quit_game_button.center))

    while RUN:
        clock.tick(FPS)
        pos_mous = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if options_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 260))
                        SCREEN.blit(text_surface[3], text_surface[3].get_rect(center=options_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 260))
                        SCREEN.blit(text_surface[3], text_surface[3].get_rect(center=options_button.center))
                        options_main()
                        RUN = False

            if recourcpack_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 320))
                        SCREEN.blit(text_surface[4], text_surface[4].get_rect(center=recourcpack_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 320))
                        SCREEN.blit(text_surface[4], text_surface[4].get_rect(center=recourcpack_button.center))
                        print('recourcpack')
                        # RUN = False
                        # recourcpack()

            if play_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 200))
                        SCREEN.blit(text_surface[5], text_surface[5].get_rect(center=play_button.center))
                        pygame.display.update()
                        SCREEN.blit(textures[4], (239, 200))
                        SCREEN.blit(text_surface[5], text_surface[5].get_rect(center=play_button.center))
                        RUN = False
                        run_game(red, blue)

            if quit_game_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 380))
                        SCREEN.blit(text_surface[2], text_surface[2].get_rect(center=quit_game_button.center))
                        pygame.display.update()

                        RUN = False
                        SCREEN.blit(textures[4], (239, 380))
                        SCREEN.blit(text_surface[2], text_surface[2].get_rect(center=quit_game_button.center))

            if event.type == pygame.QUIT:
                RUN = False

        pygame.display.update()
    pygame.quit()


# --------------------------------------------------------------------------------------------------------------------------------------
# Loading screen
# --------------------------------------------------------------------------------------------------------------------------------------
def loading_screen():
    x = threading.Thread(target=load_stuf())
    x.start()

    clock = pygame.time.Clock()
    clock.tick()
    loading_proces = 0
    SCREEN.blit(pygame.image.load(os.path.join(f"{resourcpack_folder}\Loadingscreen.png")),(0,0))
    pygame.display.update()

    while loading_proces <= 100:
        loading_proces += random.randint(1,5)
        pygame.draw.rect(SCREEN, (0,0,0),(171,382,558 / 100 * loading_proces,16))
        pygame.display.update()
        clock.tick(60)
    Game_While_Running()
    pygame.quit()


# --------------------------------------------------------------------------------------------------------------------------------------
# reourcepack
# --------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------
# Optons
# --------------------------------------------------------------------------------------------------------------------------------------
def options_main():
    clock = pygame.time.Clock()
    options_run = True

    SCREEN.blit(textures[6],(0,0))

    SCREEN.blit(textures[4], (239, 230))
    volume_button = pygame.Rect(239, 230, 422, 50)
    SCREEN.blit(text_surface[8], text_surface[8].get_rect(center=volume_button.center))

    SCREEN.blit(textures[4], (239, 290))
    language_button = pygame.Rect(239, 290, 422, 50)
    SCREEN.blit(text_surface[9], text_surface[9].get_rect(center=language_button.center))

    SCREEN.blit(textures[4], (239, 350))
    keybinds_button = pygame.Rect(239, 350, 422, 50)
    SCREEN.blit(text_surface[10], text_surface[10].get_rect(center=keybinds_button.center))

    SCREEN.blit(textures[4], (239, 410))
    back_button = pygame.Rect(239, 410, 422, 50)
    SCREEN.blit(text_surface[6], text_surface[6].get_rect(center=back_button.center))

    while options_run:
        clock.tick(FPS)
        pos_mous = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if volume_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 230))
                        SCREEN.blit(text_surface[8], text_surface[8].get_rect(center=volume_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 230))
                        SCREEN.blit(text_surface[8], text_surface[8].get_rect(center=volume_button.center))
                        print('volume button pressed')
                        #options_run = False

            if language_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 290))
                        SCREEN.blit(text_surface[9], text_surface[9].get_rect(center=language_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 290))
                        SCREEN.blit(text_surface[9], text_surface[9].get_rect(center=language_button.center))
                        print('language button pressed')
                        #options_run = False

            if keybinds_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 350))
                        SCREEN.blit(text_surface[10], text_surface[10].get_rect(center=keybinds_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 350))
                        SCREEN.blit(text_surface[10], text_surface[10].get_rect(center=keybinds_button.center))
                        print('keybinds button pressed')
                        #options_run = False

            if back_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 410))
                        SCREEN.blit(text_surface[6], text_surface[6].get_rect(center=back_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 410))
                        SCREEN.blit(text_surface[6], text_surface[6].get_rect(center=back_button.center))
                        Game_While_Running()
                        options_run = False

            if event.type == pygame.QUIT:
                options_run = False

        pygame.display.update()
    pygame.quit()


def options_esc(red, blue):
    clock = pygame.time.Clock()
    options_run = True

    SCREEN.blit(textures[6], (0, 0))

    SCREEN.blit(textures[4], (239, 230))
    volume_button = pygame.Rect(239, 230, 422, 50)
    SCREEN.blit(text_surface[8], text_surface[8].get_rect(center=volume_button.center))

    SCREEN.blit(textures[4], (239, 290))
    language_button = pygame.Rect(239, 290, 422, 50)
    SCREEN.blit(text_surface[9], text_surface[9].get_rect(center=language_button.center))

    SCREEN.blit(textures[4], (239, 350))
    keybinds_button = pygame.Rect(239, 350, 422, 50)
    SCREEN.blit(text_surface[10], text_surface[10].get_rect(center=keybinds_button.center))

    SCREEN.blit(textures[4], (239, 410))
    back_button = pygame.Rect(239, 410, 422, 50)
    SCREEN.blit(text_surface[6], text_surface[6].get_rect(center=back_button.center))

    while options_run:
        clock.tick(FPS)
        pos_mous = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if volume_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 230))
                        SCREEN.blit(text_surface[8], text_surface[8].get_rect(center=volume_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 230))
                        SCREEN.blit(text_surface[8], text_surface[8].get_rect(center=volume_button.center))
                        print('volume button pressed')
                        # options_run = False

            if language_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 290))
                        SCREEN.blit(text_surface[9], text_surface[9].get_rect(center=language_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 290))
                        SCREEN.blit(text_surface[9], text_surface[9].get_rect(center=language_button.center))
                        print('language button pressed')
                        # options_run = False

            if keybinds_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 350))
                        SCREEN.blit(text_surface[10], text_surface[10].get_rect(center=keybinds_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 350))
                        SCREEN.blit(text_surface[10], text_surface[10].get_rect(center=keybinds_button.center))
                        print('keybinds button pressed')
                        # options_run = False

            if back_button.collidepoint(pos_mous):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        SCREEN.blit(textures[5], (239, 410))
                        SCREEN.blit(text_surface[6], text_surface[6].get_rect(center=back_button.center))
                        pygame.display.update()

                        SCREEN.blit(textures[4], (239, 410))
                        SCREEN.blit(text_surface[6], text_surface[6].get_rect(center=back_button.center))
                        esc_menue(red,blue)
                        options_run = False

            if event.type == pygame.QUIT:
                options_run = False

        pygame.display.update()
    pygame.quit()

# --------------------------------------------------------------------------------------------------------------------------------------
# Game Starten
# --------------------------------------------------------------------------------------------------------------------------------------
loading_screen()