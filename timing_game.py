import pygame
import sys

pygame.init()
pygame.display.set_caption("timing_game")
screen = pygame.display.set_mode((1000,500))

# font configure
judge_font = pygame.font.SysFont(None, 24)
judge_text = {
        "s":judge_font.render("S",True,(255,255,0)),
        "a":judge_font.render("A",True,(255,0,0)),
        "b":judge_font.render("B",True,(0,0,255)),
        "c":judge_font.render("C",True,(0,255,0))
        }

# color 
RED = (255,0,0) 
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

# the position of the timing bar
timing_bar_x = 100
timing_bar_y = 300 
timing_bar_width = 800
timing_bar_height = 100

bar_pos = 0
bar_width = 3
counter_flag = True
shot_flag = False
hit_pos = 0 

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hit_pos = bar_pos 
                shot_flag = True

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # background of the timing bar
    pygame.draw.rect(screen, WHITE, 
            pygame.Rect(timing_bar_x,timing_bar_y, 
                        timing_bar_width, timing_bar_height))
            
    # aiming bar
    pygame.draw.line(screen, RED, 
            (bar_pos + timing_bar_x, timing_bar_y),
            (bar_pos + timing_bar_x, timing_bar_y + timing_bar_height),
            width=bar_width)

    center_pos = timing_bar_width/2 + timing_bar_x 
    
    # s line
    s_gap = 10
    a_gap = 30
    b_gap = 70
    
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

    if shot_flag:
        pygame.draw.line(screen, GREEN,
                (hit_pos + timing_bar_x, timing_bar_y),
                (hit_pos + timing_bar_x, timing_bar_y + timing_bar_height),
                width=bar_width)

        distance = abs(hit_pos-(timing_bar_width/2))
        if distance < s_gap:
            screen.blit(judge_text["s"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        elif distance < a_gap:
            screen.blit(judge_text["a"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        elif distance < b_gap:
            screen.blit(judge_text["b"],(hit_pos + timing_bar_x, timing_bar_y + 140))
        else:
            screen.blit(judge_text["c"],(hit_pos + timing_bar_x, timing_bar_y + 140))

    pygame.display.update()
    screen.fill(BLACK)

    if counter_flag:
        if bar_pos < timing_bar_width - bar_width:
            bar_pos += 1
        else:
            bar_pos = 0
        counter_flag = False
    else:
        counter_flag = True


