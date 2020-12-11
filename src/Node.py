import random
import pygame
from pygame import gfxdraw
from globals import *

class Node(object):
    # A node object contains data for each node
    def __init__(self, pos=(1,1), vel=(1,1), color=RED, radius=10, text="A"):
        self.pos    = pos # This position is the center of the node
        self.vel    = vel # Velocity vector
        self.color  = color
        self.radius = radius
        self.text   = text
        self.updateB= True
        self.font   = pygame.font.SysFont(None, int(self.radius * 2.4))

    def update(self, dt):
        if (self.updateB):
            if (self.pos[0] <= 0):
                self.vel = (random.uniform(NODE_MIN_VEL, NODE_MAX_VEL), self.vel[1])
            if (self.pos[0] >= WIDTH):
                self.vel = (-random.uniform(NODE_MIN_VEL, NODE_MAX_VEL), self.vel[1])
            if (self.pos[1] <= 0):
                self.vel = (self.vel[0], random.uniform(NODE_MIN_VEL, NODE_MAX_VEL))
            if (self.pos[1] >= HEIGHT):
                self.vel = (self.vel[0], -random.uniform(NODE_MIN_VEL, NODE_MAX_VEL))

            x = self.pos[0] + self.vel[0] * dt
            y = self.pos[1] + self.vel[1] * dt
            self.pos = (x,y)

    def draw(self, surface):
        # Draw the node
        gfxdraw.aacircle(surface, int(self.pos[0]), int(self.pos[1]), self.radius, self.color)
        gfxdraw.filled_circle(surface, int(self.pos[0]), int(self.pos[1]), self.radius, self.color)

        # Draw the text at the center of the node
        textItem = self.font.render(self.text[0], True, BLACK)
        textWidth = textItem.get_rect().width
        textHeight = textItem.get_rect().height
        surface.blit(textItem, (int(self.pos[0] - textWidth/2), int(self.pos[1] - textHeight/2)))


