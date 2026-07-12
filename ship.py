import pygame

class Ship:
    """管理飞船的类。"""

    def __init__(self, game):
        """初始化飞船并设置初始位置。"""
        self.screen = game.screen
        self.settings = game.settings

        self.screen_rect = game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x,y中存储一个浮点数。
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志（飞船一开始不移动）。
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        """
        # 加载角色图像并获取其外接矩形
        self.image2 = pygame.image.load('images/hero.bmp')
        self.rect2 = self.image2.get_rect()

        # 角色放在屏幕右上方
        self.rect2.bottomright = self.screen_rect.bottomright
        """
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 5:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        #根据self.x/y更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        # self.screen.blit(self.image2, self.rect2)
