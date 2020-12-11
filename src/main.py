# Author: Logan Hunt

import pygame
from Graph import Graph
from Node import Node
from globals import * # Global variables

pygame.init()

def main():
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    running = True
    update = True
    graph = Graph(screen, file="finalGraph.txt")
    graph.fromFile()
    graph.updateHashLinks()

    nodeUnderMouse = None

    while(running):
        # Main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user closed the window
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    searchTerm = input("What would you like to search for? ")
                    for i in graph.nodes:
                        if searchTerm in i.text:
                            graph.nodesUnderMouse.append(i)
                if event.key == pygame.K_c:
                    graph.nodesUnderMouse = []
                if event.key == pygame.K_SPACE:
                    if (update):
                        update = False
                    else:
                        update = True
                if event.key == pygame.K_p:
                    for i in graph.nodes:
                        if (i not in graph.nodesUnderMouse):
                            graph.nodesUnderMouse.append(i)

            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                for i in graph.nodes:
                    if(mouseX > i.pos[0] - i.radius and \
                            mouseY > i.pos[1] - i.radius and \
                            mouseX < i.pos[0] + i.radius and \
                            mouseY < i.pos[1] + i.radius):
                        i.updateB = False
                        if (i not in graph.nodesUnderMouse):
                            graph.nodesUnderMouse.append(i)
                    else:
                        if i in graph.nodesUnderMouse:
                            graph.nodesUnderMouse.remove(i)
                        i.updateB = True

        screen.fill(BLACK)

        if (update):
            graph.updateNodePositions(1)
        graph.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
