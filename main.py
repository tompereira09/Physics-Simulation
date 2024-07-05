import pygame as pg
import time
#TODO: Tween the fall of the ball


class Ball:
    def __init__(self, sc, color : tuple, pos : tuple, radius : int, weight : int) -> None:
        self.sc = sc
        self.color = color
        self.pos = pos
        self.radius = radius
        self.weight = weight

        pg.draw.circle(sc, color, pos, radius)

        self.x = pos[0]
        self.y = pos[1]

        self.potential_energy = 100
        self.kinetic_energy = 0

    def fall(self, increment):
        if self.y < 870:
            self.y += increment * self.weight * self.kinetic_energy
            if self.kinetic_energy <= 100:
                self.kinetic_energy += increment
                self.potential_energy -= increment

            self.sc.fill((125, 146, 163))
            pg.draw.rect(self.sc, (35, 35, 35), pg.Rect(0, 910, 1000, 40))

            pg.draw.circle(self.sc, self.color, (self.x, self.y), self.radius)

            pg.display.flip()

        else:
            self.y = self.pos[1]
            self.kinetic_energy = 0
            self.potential_energy = 100
            pg.display.flip()
            time.sleep(1)


class App:
    def __init__(self, res : tuple):
        pg.init()
        self.sc = pg.display.set_mode(res)
        pg.display.set_caption("Physics Engine.")
        self.sc.fill((125, 146, 163))
        pg.display.flip()

        ball1 = Ball(self.sc, (35, 35, 35), (500, 80), 10, 1)


        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    quit()

            ball1.fall(1)
            print(ball1.y)
            time.sleep(0.01)
            pg.display.flip()


App((1000, 1000))
