#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
像素画编辑器
使用pygame实现的像素艺术编辑工具
"""

import pygame
import os

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

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("像素画编辑器")

clock = pygame.time.Clock()
font = get_chinese_font(24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, WHITE]
current_color = BLACK

grid_size = 32
cols = 20
rows = 15
grid = [[WHITE for _ in range(rows)] for _ in range(cols)]

def draw_grid():
    for x in range(cols):
        for y in range(rows):
            rect = (50 + x * grid_size, 50 + y * grid_size, grid_size - 1, grid_size - 1)
            pygame.draw.rect(screen, grid[x][y], rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_color_palette():
    for i, color in enumerate(colors):
        rect = (700, 50 + i * 50, 40, 40)
        pygame.draw.rect(screen, color, rect)
        if color == current_color:
            pygame.draw.rect(screen, BLACK, rect, 3)

def draw_ui():
    text = font.render("像素画编辑器", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
    
    clear_text = font.render("清空 (C)", True, BLACK)
    pygame.draw.rect(screen, GRAY, (700, 500, 150, 40))
    screen.blit(clear_text, (710, 505))

drawing = False
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            mx, my = pygame.mouse.get_pos()
            
            if 700 <= mx <= 740:
                color_idx = (my - 50) // 50
                if 0 <= color_idx < len(colors):
                    current_color = colors[color_idx]
            
            if 700 <= mx <= 850 and 500 <= my <= 540:
                grid = [[WHITE for _ in range(rows)] for _ in range(cols)]
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                grid = [[WHITE for _ in range(rows)] for _ in range(cols)]
    
    if drawing:
        mx, my = pygame.mouse.get_pos()
        grid_x = (mx - 50) // grid_size
        grid_y = (my - 50) // grid_size
        if 0 <= grid_x < cols and 0 <= grid_y < rows:
            grid[grid_x][grid_y] = current_color
    
    draw_grid()
    draw_color_palette()
    draw_ui()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
