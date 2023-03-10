import pygame
import random
import sys

pygame.init()
pygame.display.set_caption("timing_game")
screen = pygame.display.set_mode((1000,500))

# mixer 
pygame.mixer.init(44100)
pygame.mixer.music.load("./sounds/music/texture1.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)
player_attack = False 
player_attack_cycle = 0.0

# images
player_char_img = pygame.image.load("./img/me.png")
enemy_char_img = pygame.image.load("./img/enemy.png")

# font configure
judge_font = pygame.font.SysFont(None, 24)
judge_text = {
        "s":judge_font.render("S",True,(255,255,0)),
        "a":judge_font.render("A",True,(255,0,0)),
        "b":judge_font.render("B",True,(0,0,255)),
        "c":judge_font.render("C",True,(0,255,0))
        }

damage_font  = pygame.font.SysFont(None, 24)
system_font = pygame.font.SysFont(None,24)

op_text = system_font.render("Timing Game", True,(255,255,255))
clear_text = system_font.render("Game Clear!",True,(255,255,255))

# color 
RED = (255,0,0) 
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

# timing bar 
timing_bar_x = 100
timing_bar_y = 300 
timing_bar_width = 800
timing_bar_height = 100
bar_pos = 0
bar_width = 3
hit_pos = 0 
counter_flag = True
shot_flag = False
s_gap = 10
a_gap = 30
b_gap = 70


enemy_attack = False
enemy_attack_cycle = 0.0

# hp
enemy_hp = 100

process = 0
attack_flag = False
shot_flag = False


def draw_player():
    global player_attack, player_attack_cycle 

    screen.blit(player_char_img,(700-(int(player_attack_cycle)*20),100))

    if player_attack and (player_attack_cycle<5):
        player_attack_cycle += 0.03
    else:
        player_attack = False
        player_attack_cycle = 0

def draw_enemy():
    global enemy_attack, enemy_attack_cycle

    screen.blit(enemy_char_img,(200+(int(enemy_attack_cycle)*20),100)) 

    if enemy_attack and (enemy_attack_cycle<5):
        enemy_attack_cycle += 0.03
    else:
        enemy_attack = False
        enemy_attack_cycle = 0

def draw_timing_bar():

    # background of the timing bar
    pygame.draw.rect(screen, WHITE, 
            pygame.Rect(timing_bar_x,timing_bar_y, 
                        timing_bar_width, timing_bar_height))
            
    # aiming bar
    pygame.draw.line(screen, RED, 
            (bar_pos + timing_bar_x, timing_bar_y),
            (bar_pos + timing_bar_x, timing_bar_y + timing_bar_height),
            width=bar_width)


def damage_calc(score):
    global enemy_hp, attack_flag, process
    
    if not(attack_flag):

        if score == 's':
            damage = random.randint(25,35)
        elif score == 'a':
            damage = random.randint(15,25)
        elif score == 'b':
            damage = random.randint(5,15)
        else:
            damage = random.randint(1,5)

        enemy_hp -= damage 
        if enemy_hp < 0:
            process += 1

    attack_flag = True


def calc_bar_position():
    global counter_flag, timing_bar_width, bar_width, bar_pos
    global attack_flag, shot_flag 

    if counter_flag:
        if bar_pos < timing_bar_width - bar_width:
            bar_pos += 1
        else:
            bar_pos = 0
            attack_flag = False
            shot_flag = False
        counter_flag = False
    else:
        counter_flag = True

def draw_lines():
    global s_gap, a_gap, b_gap 
    global timing_bar_width, timing_bar_x     

    center_pos = timing_bar_width/2 + timing_bar_x 

    a_line_len = timing_bar_height - 60 
    b_line_len = timing_bar_height - 25 

    pygame.draw.line(screen, BLUE,
            (center_pos - s_gap, timing_bar_y),
            (center_pos - s_gap, timing_bar_y + timing_bar_height),
            width=bar_width)

    pygame.draw.line(screen, BLUE,
            (center_pos + s_gap, timing_bar_y),
            (center_pos + s_gap, timing_bar_y + timing_bar_height),
            width=bar_width)

    # a lines
    pygame.draw.line(screen, BLUE,
            (center_pos - a_gap, timing_bar_y + a_line_len/2),
            (center_pos - a_gap, timing_bar_y + timing_bar_height - a_line_len/2),
            width=bar_width)

    pygame.draw.line(screen, BLUE,
            (center_pos + a_gap, timing_bar_y + a_line_len/2),
            (center_pos + a_gap, timing_bar_y + timing_bar_height - a_line_len/2),
            width=bar_width)

    # b lines
    pygame.draw.line(screen, BLUE,
            (center_pos - b_gap, timing_bar_y + b_line_len/2),
            (center_pos - b_gap, timing_bar_y + timing_bar_height - b_line_len/2),
            width=bar_width)

    pygame.draw.line(screen, BLUE,
            (center_pos + b_gap, timing_bar_y + b_line_len/2),
            (center_pos + b_gap, timing_bar_y + timing_bar_height - b_line_len/2),
            width=bar_width)


def hit_check(hit_pos): 
    global s_gap, a_gap, b_gap

    distance = abs(hit_pos-(timing_bar_width/2))

    if distance < s_gap:
        screen.blit(judge_text["s"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        score = "s"
    elif distance < a_gap:
        screen.blit(judge_text["a"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        score = "a"
    elif distance < b_gap:
        screen.blit(judge_text["b"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        score = "b"
    else:
        screen.blit(judge_text["c"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        score = "c"

    return score

op_timer = 1000

while True:

    op_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) and not (attack_flag):
                hit_pos = bar_pos 
                shot_flag = True
                player_attack = True
                attack_flag = False

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if process == 0:
        
        screen.blit(op_text,(450,250))
        pygame.display.update()
        screen.fill(BLACK)

        if op_timer == 0:
            process += 1

    if process == 1:


        draw_enemy()
        draw_player()
        draw_timing_bar()
        draw_lines()


        calc_bar_position()

        if shot_flag:
            pygame.draw.line(screen, GREEN,
                    (hit_pos + timing_bar_x, timing_bar_y),
                    (hit_pos + timing_bar_x, timing_bar_y + timing_bar_height),
                    width=bar_width)
            
            score = hit_check(hit_pos)

            damage_calc(score)


        damage_text = damage_font.render(str(enemy_hp),True,(255,0,0))
        screen.blit(damage_text,(200,10))

        pygame.display.update()
        screen.fill(BLACK)



    elif process == 2:

        screen.blit(clear_text,(450,250))
        pygame.display.update()
        screen.fill(BLACK)





