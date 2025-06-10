import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    cha_img = pg.image.load("fig/3.png")
    cha_img = pg.transform.flip(cha_img, True, False)
    tmr = 0
    x = 0
    cha_rct = cha_img.get_rect()
    cha_rct.center = (300, 200)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        x1 = 0
        y1 = 0

        x1 -= 1

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            y1 -= 1
        if key_lst[pg.K_LEFT]:
            x1 -= 1
        if key_lst[pg.K_RIGHT]:
            x1 += 2
        if key_lst[pg.K_DOWN]:
            y1 += 1

        cha_rct.move_ip(x1, y1)

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(cha_img, cha_rct)
        pg.display.update()
        tmr += 1      
        clock.tick(200)

        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()