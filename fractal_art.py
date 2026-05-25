#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分形艺术
使用pygame实现的分形图案绘制游戏
"""

import pygame
import os
import math

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
pygame.display.set_caption("分形艺术")

clock = pygame.time.Clock()
font = get_chinese_font(24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_mandelbrot():
    scale = 200
    for x in range(WIDTH):
        for y in range(HEIGHT):
            zx, zy = 0, 0
            cx = (x - WIDTH/2) / scale
            cy = (y - HEIGHT/2) / scale
            
            iteration = 0
            max_iter = 50
            
            while zx*zx + zy*zy < 4 and iteration < max_iter:
                temp = zx*zx - zy*zy + cx
                zy = 2*zx*zy + cy
                zx = temp
                iteration += 1
            
            if iteration == max_iter:
                color = BLACK
            else:
                color = (
                    (iteration * 5) % 255,
                    (iteration * 7) % 255,
                    (iteration * 11) % 255
                )
            screen.set_at((x, y), color)

draw_mandelbrot()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_mandelbrot()
    
    text = font.render("按空格键重新生成", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
