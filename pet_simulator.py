#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
宠物模拟器
使用pygame实现的电子宠物游戏
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
pygame.display.set_caption("宠物模拟器")

clock = pygame.time.Clock()
font = get_chinese_font(28)
small_font = get_chinese_font(20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
YELLOW = (255, 200, 100)
PINK = (255, 200, 200)

pet_x = WIDTH // 2
pet_y = HEIGHT // 2
hunger = 100
happiness = 100
energy = 100

def draw_pet():
    pygame.draw.circle(screen, PINK, (pet_x, pet_y), 60)
    pygame.draw.circle(screen, BLACK, (pet_x - 20, pet_y - 10), 8)
    pygame.draw.circle(screen, BLACK, (pet_x + 20, pet_y - 10), 8)
    pygame.draw.circle(screen, RED, (pet_x, pet_y + 15), 12, 3)
    
    if happiness > 50:
        pygame.draw.arc(screen, BLACK, (pet_x - 20, pet_y + 10, 40, 20), 3.14, 0, 2)

def draw_stats():
    pygame.draw.rect(screen, GRAY, (50, 50, 200, 30))
    pygame.draw.rect(screen, GREEN, (50, 50, hunger*2, 30))
    text = small_font.render(f"饥饿: {hunger}", True, BLACK)
    screen.blit(text, (50, 85))
    
    pygame.draw.rect(screen, GRAY, (50, 120, 200, 30))
    pygame.draw.rect(screen, YELLOW, (50, 120, happiness*2, 30))
    text = small_font.render(f"快乐: {happiness}", True, BLACK)
    screen.blit(text, (50, 155))
    
    pygame.draw.rect(screen, GRAY, (50, 190, 200, 30))
    pygame.draw.rect(screen, BLUE, (50, 190, energy*2, 30))
    text = small_font.render(f"精力: {energy}", True, BLACK)
    screen.blit(text, (50, 225))

def draw_buttons():
    buttons = [
        ("喂食", (50, 350, 100, 50), GREEN),
        ("玩耍", (170, 350, 100, 50), YELLOW),
        ("睡觉", (290, 350, 100, 50), BLUE)
    ]
    
    for text, rect, color in buttons:
        pygame.draw.rect(screen, color, rect)
        text_surf = small_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=(rect[0]+50, rect[1]+25))
        screen.blit(text_surf, text_rect)
    
    return buttons

buttons = draw_buttons()

time_counter = 0
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            if 50 <= mx <= 150 and 350 <= my <= 400:
                hunger = min(100, hunger + 20)
            elif 170 <= mx <= 270 and 350 <= my <= 400:
                if energy > 10:
                    happiness = min(100, happiness + 15)
                    energy = max(0, energy - 10)
            elif 290 <= mx <= 390 and 350 <= my <= 400:
                energy = min(100, energy + 30)
    
    time_counter += 1
    if time_counter % 60 == 0:
        hunger = max(0, hunger - 1)
        happiness = max(0, happiness - 1)
        energy = max(0, energy - 1)
    
    draw_pet()
    draw_stats()
    buttons = draw_buttons()
    
    title = font.render("我的电子宠物", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
