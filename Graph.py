import math
import random
import pygame
from parse import parse_input
from Node import Node
from globals import *

def createColorFromString(s):
    i = hash(s)
    r = (i & 0xFF0000) >> 16
    g = (i & 0x00FF00) >> 8
    b = (i & 0x0000FF) + 125;
    return (r,g,b%125 + 100)

def generateRandomVelocity():
    dx = random.uniform(NODE_MIN_VEL, NODE_MAX_VEL)
    dy = random.uniform(NODE_MIN_VEL, NODE_MAX_VEL)
    randomVelocity = (dx, dy)
    return randomVelocity

class Graph(object):
    # A directed graph which contains nodes
    def __init__(self, surface, nodes=[], links=[], file=""):
        self.surface = surface
        self.nodes   = nodes
        self.links   = links
        self.hashLink= {} # This will provide faster access to links
        self.file    = file
        self.font    = pygame.font.SysFont(None, 15)

        self.nodesUnderMouse = []

    def fromFile(self, initializeWithRandomVels=True):
        # Parse from file
        self.nodes, self.links = parse_input(self.file)

        # Set the position of each node
        square = math.ceil(math.sqrt(len(self.nodes)))
        for i in range(square):
            for j in range(square):
                if (i*square + j < len(self.nodes)):
                    self.nodes[i*square + j].pos = (int((WIDTH)/(square) * i + 20), int((HEIGHT)/(square) * j + 20))
                    if (initializeWithRandomVels):
                        self.nodes[i*square + j].vel = generateRandomVelocity()
                    else:
                        self.nodes[i*square + j].vel = (0, 0)
                    self.nodes[i*square + j].color = createColorFromString(self.nodes[square*i + j].text)


    def updateNodePositions(self, dt):
        for i in self.nodes:
            i.update(dt) # Update the position for velocity

    def randomNodes(self):
        # Populate nodes with random ones
        for i in range(10):
            for j in range(10):
                position = (20 + i * 80, 20 + j * 80)
                color=random.choice([RED,GREEN,BLUE])
                radius=random.randint(5, 15)
                text=random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
                self.nodes.append(Node(position, generateRandomVelocity(), color, radius, text))

    def randomLinks(self):
        for i in range(random.randint(1, 1000)):
            # Each link is (source, destination, weight)
            self.links.append((random.choice(self.nodes), random.choice(self.nodes), 1, "BRUH"))

    def updateHashLinks(self):
        # This will also calculate the radius for each node
        for i in self.links:
            # Hash links appear in the dictionary as:
            # source_node : [(node1, weight1, description1), (node2, weight2, description2)]
            if (i[0] not in self.hashLink.keys()):
                self.hashLink[i[0]] = []
            self.hashLink[i[0]].append((i[1], i[2], i[3]))
        for i in self.nodes:
            if (i in self.hashLink.keys()):
                i.radius = max(min(len(self.hashLink[i]), NODE_MAX_RADIUS), NODE_MIN_RADIUS)
            else:
                # The node has no outer links
                i.radius = NODE_MIN_RADIUS

    def drawLinks(self, node):
        # Draw all of the links from one node to all of its neighbors
        if (node in self.hashLink.keys()):
            for i in self.hashLink[node]:
                pygame.gfxdraw.line(self.surface, int(node.pos[0]), int(node.pos[1]), int(i[0].pos[0]), int(i[0].pos[1]), RED)
                midPoint = ((i[0].pos[0] + node.pos[0])/2, (i[0].pos[1] + node.pos[1])/2)
                render=self.font.render(i[0].text, True, WHITE)
                self.surface.blit(render, midPoint)
                render=self.font.render(i[2], True, WHITE)
                self.surface.blit(render, (midPoint[0] + 10, midPoint[1]+10))
        else:
            for i in self.links:
                if i[0] == node:
                    pygame.gfxdraw.line(self.surface, int(node.pos[0]), int(node.pos[1]), int(i[1].pos[0]), int(i[1].pos[1]), RED)
                    midPoint = (abs(i[1].pos[0] + node.pos[0])/2, abs(i[1].pos[1] + node.pos[1])/2)
                    render=self.font.render(i[1].text, True, WHITE)
                    self.surface.blit(render, midPoint)
                    render=self.font.render(i[3], True, WHITE)
                    self.surface.blit(render, (midPoint[0] + 10, midPoint[1]+10))

    def draw(self):
        # Draw the graph for i in nodes:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        if (self.nodesUnderMouse):
            # If the node is under the mouse draw the links and the node
            # content
            for i in self.nodesUnderMouse:
                self.drawLinks(i)
                node=i
                render=self.font.render(node.text, True, WHITE)
                self.surface.blit(render, (node.pos[0]+node.radius, node.pos[1]+node.radius))

        # Now we can finally draw the nodes!
        for i in self.nodes:
            i.draw(self.surface)

