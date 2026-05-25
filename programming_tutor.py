#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编程导师
使用pygame实现的编程学习工具
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
pygame.display.set_caption("编程导师")

clock = pygame.time.Clock()
font = get_chinese_font(24)
small_font = get_chinese_font(18)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
YELLOW = (255, 255, 100)

lessons = [
    {
        "title": "第一课: 打印 Hello World!",
        "explanation": "这是每个程序员的第一步！",
        "code": "print('Hello World!')",
        "output": "Hello World!"
    },
    {
        "title": "第二课: 变量",
        "explanation": "变量用来存储数据。",
        "code": "x = 5\nprint(x)",
        "output": "5"
    },
    {
        "title": "第三课: 循环",
        "explanation": "循环可以重复执行代码。",
        "code": "for i in range(3):\n    print('Hi!')",
        "output": "Hi!\nHi!\nHi!"
    },
    {
        "title": "第四课: 条件语句",
        "explanation": "根据条件做不同的事情。",
        "code": "age = 18\nif age >= 18:\n    print('成年')",
        "output": "成年"
    }
]

current_lesson = 0

def draw_lesson():
    lesson = lessons[current_lesson]
    
    title = font.render(lesson["title"], True, BLACK)
    screen.blit(title, (50, 30))
    
    exp = small_font.render(lesson["explanation"], True, (50, 50, 50))
    screen.blit(exp, (50, 70))
    
    pygame.draw.rect(screen, (240, 240, 240), (50, 100, 800, 180))
    pygame.draw.rect(screen, GRAY, (50, 100, 800, 180), 2)
    code_lines = lesson["code"].split('\n')
    for i, line in enumerate(code_lines):
        text = small_font.render(line, True, BLACK)
        screen.blit(text, (70, 120 + i * 30))
    
    pygame.draw.rect(screen, BLACK, (50, 320, 800, 180))
    pygame.draw.rect(screen, GRAY, (50, 320, 800, 180), 2)
    output_lines = lesson["output"].split('\n')
    for i, line in enumerate(output_lines):
        text = small_font.render(line, True, GREEN)
        screen.blit(text, (70, 340 + i * 30))

def draw_navigation():
    pygame.draw.rect(screen, BLUE, (50, 520, 100, 50))
    prev_text = font.render("上一页", True, WHITE)
    text_rect = prev_text.get_rect(center=(100, 545))
    screen.blit(prev_text, text_rect)
    
    pygame.draw.rect(screen, GREEN, (750, 520, 100, 50))
    next_text = font.render("下一页", True, WHITE)
    text_rect = next_text.get_rect(center=(800, 545))
    screen.blit(next_text, text_rect)
    
    page_text = font.render(f"{current_lesson + 1} / {len(lessons)}", True, BLACK)
    text_rect = page_text.get_rect(center=(WIDTH // 2, 545))
    screen.blit(page_text, text_rect)

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            if 50 <= mx <= 150 and 520 <= my <= 570:
                current_lesson = max(0, current_lesson - 1)
            elif 750 <= mx <= 850 and 520 <= my <= 570:
                current_lesson = min(len(lessons) - 1, current_lesson + 1)
    
    draw_lesson()
    draw_navigation()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
