#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
化学实验室
使用pygame实现的化学实验游戏
"""

import pygame
import os
import random

pygame.init()

# 尝试使用中文字体
def get_chinese_font(size):
    """获取支持中文的字体"""
    font_names = [
        "C:/Windows/Fonts/simsun.ttc",  # 宋体
        "C:/Windows/Fonts/msyh.ttc",    # 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",  # 黑体
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",  # Linux
        "/System/Library/Fonts/PingFang.ttc",  # macOS
    ]
    for font_name in font_names:
        if os.path.exists(font_name):
            try:
                return pygame.font.Font(font_name, size)
            except:
                continue
    return pygame.font.Font(None, size)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("化学实验室")

clock = pygame.time.Clock()
font = get_chinese_font(28)
small_font = get_chinese_font(20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 100, 100)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)

elements = ['H', 'O', 'C', 'N', 'Na', 'Cl']
selected_elements = []

beaker_color = BLUE
reaction_happened = False

def draw_beaker(x, y, width, height, color):
    pygame.draw.rect(screen, (200, 200, 255), (x, y, width, height), 3)
    pygame.draw.rect(screen, color, (x+5, y+5, width-10, height-10))

def draw_elements():
    for i, elem in enumerate(elements):
        pygame.draw.rect(screen, GRAY, (50 + i*100, 50, 80, 60))
        text = font.render(elem, True, BLACK)
        text_rect = text.get_rect(center=(90 + i*100, 80))
        screen.blit(text, text_rect)

def draw_selected():
    text = small_font.render(f"选中: {' + '.join(selected_elements)}", True, BLACK)
    screen.blit(text, (50, 150))
    
    if len(selected_elements) >= 2:
        button_text = font.render("混合!", True, WHITE)
        pygame.draw.rect(screen, GREEN, (300, 180, 200, 60))
        text_rect = button_text.get_rect(center=(400, 210))
        screen.blit(button_text, text_rect)

def check_reaction():
    global beaker_color, reaction_happened, selected_elements
    if 'H' in selected_elements and 'O' in selected_elements:
        beaker_color = (0, 150, 255)
        reaction_text = "H₂O 水生成了!"
    elif 'Na' in selected_elements and 'Cl' in selected_elements:
        beaker_color = (255, 200, 100)
        reaction_text = "NaCl 盐生成了!"
    elif 'C' in selected_elements and 'O' in selected_elements:
        beaker_color = (100, 100, 100)
        reaction_text = "CO₂ 二氧化碳生成了!"
    else:
        beaker_color = BLUE
        reaction_text = "没有明显反应"
    
    reaction_happened = True
    selected_elements = []
    return reaction_text

reaction_display_text = ""
reaction_timer = 0

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for i, elem in enumerate(elements):
                if 50 + i*100 <= mx <= 130 + i*100 and 50 <= my <= 110:
                    if elem in selected_elements:
                        selected_elements.remove(elem)
                    else:
                        selected_elements.append(elem)
            if len(selected_elements) >= 2 and 300 <= mx <= 500 and 180 <= my <= 240:
                reaction_display_text = check_reaction()
                reaction_timer = 120
    
    draw_elements()
    draw_selected()
    
    if reaction_display_text:
        reaction_timer -= 1
        if reaction_timer > 0:
            text = font.render(reaction_display_text, True, RED)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
            screen.blit(text, text_rect)
    
    draw_beaker(300, 300, 200, 200, beaker_color)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
