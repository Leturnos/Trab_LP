#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        sorteio = random.randint(0,1)
        if sorteio == 0:
            self.move_control = True
        else:
            self.move_control = False

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento Enemy3:
        if self.name == 'Enemy3':
            if self.move_control == True:
                self.rect.centery += (ENTITY_SPEED[self.name] * 2)
                if self.rect.bottom > WIN_HEIGHT:
                    self.move_control = False
            else:
                self.rect.centery -= ENTITY_SPEED[self.name]
                if self.rect.top < 0:
                    self.move_control = True
        
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
