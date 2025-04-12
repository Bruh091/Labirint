import pygame as pg

class GameSprait(pg.sprite.Sprite):
    def __init__(self, Iname, widht, height, speed, x, y):
        self.image = pg.transform.scale(pg.image.load(Iname), (widht, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprait):
    def move(self, keys_pressed):
        if keys_pressed[pg.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys_pressed[pg.K_d] and self.rect.x < w - w/10:
            self.rect.x += self.speed
        elif keys_pressed[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys_pressed[pg.K_s] and self.rect.y < h - h/10:
            self.rect.y += self.speed
    def PutBom(self, keys_pressed):
        if keys_pressed[pg.K_SPACE]:
            pass
            # bomb = Bom('bom.png', w/10, h/10, 0, self.rect.x, self.rect.y)
            # bombs.append[bomb]


class Enemy(GameSprait):
    def move(self, keys_pressed):
        self.rect.x += self.speed
        if self.rect.x > w - w/12:
            self.speed *= -1
        elif self.rect.x < w - w/4:
            self.speed *= -1

class Bom(GameSprait):
    def bomb(self):
        pass

class Wall(pg.sprite.Sprite):
    def __init__(self, widht, height, x, y, color):
        super().__init__()
        self.color = color
        self.image = pg.Surface((widht, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))



 

win = pg.display.set_mode((700, 500), pg.FULLSCREEN)
w, h = pg.display.get_window_size()
pg.display.set_caption('Лабиринт')

#объекты
bg = pg.transform.scale(pg.image.load('background.jpg'), (w,h))
hero = Hero("hero.png", w/10, h/10, 10, 50, h - 75)
enemy = Enemy("cyborg.png", w/10, h/10, 5, w - 75, h - 150)
gold = GameSprait("treasure.png", w/10, h/10, 10, w - 75, h - 75)
wall1 = Wall(25, h - w/10, 150, 75, (200,200,200))
wall2 = Wall(w - 350, 25, w/5 + 6, w/10+3, (200,200,200))
wall3 = Wall(25, h - w/10, w-215, 75, (200,200,200))

pg.mixer.init()
pg.mixer.music.load("jungles.ogg")
pg.mixer.music.play()
#переменные\
bombs = list()
Finish = False
run = True
clock = pg.time.Clock()
winSound = pg.mixer.Sound('money.ogg')
loseSound = pg.mixer.Sound('kick.ogg')

#game while
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                win = pg.display.set_mode((700,500))
                w = 700
                h = 500
                bg = pg.transform.scale(pg.image.load('background.jpg'), (w,h))
                hero = Hero("hero.png", w/10, h/10, 10, 50, h - 75)
                enemy = Enemy("cyborg.png", w/10, h/10, 5, w - 75, h - 150)
                gold = GameSprait("treasure.png", w/10, h/10, 10, w - 75, h - 75)

    if not Finish:
        keys_pressed = pg.key.get_pressed()

        win.blit(bg, (0,0))
        hero.move(keys_pressed)
        hero.PutBom(keys_pressed)
        enemy.move(keys_pressed)
        enemy.reset()
        wall1.reset()
        wall2.reset()
        wall3.reset()
        gold.reset()

        for b in bombs:
            b.reset()
        hero.reset()
        if pg.sprite.collide_rect(hero, gold):
            winSound.play()
            Finish = True
            victory = True
        if pg.sprite.collide_rect(hero, wall1):
            loseSound.play()
            Finish = True
            victory = False
        if pg.sprite.collide_rect(hero, wall2):
            loseSound.play()
            Finish = True
            victory = False
        if pg.sprite.collide_rect(hero, wall3):
            loseSound.play()
            Finish = True
            victory = False
        if pg.sprite.collide_rect(hero, enemy):
            loseSound.play()
            Finish = True
            victory = False
    if Finish:
        if victory:
            bg = pg.transform.scale(pg.image.load('Pob.jpg'), (w,h))
            win.blit(bg, (0,0))
        else:
            bg = pg.transform.scale(pg.image.load('gameover.jpg'), (w,h))
            win.blit(bg, (0,0))

    pg.display.update()
    clock.tick(60)