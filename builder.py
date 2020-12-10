import pygame
from Graph import Graph
from Node import Node
from globals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    graph = Graph(screen, file="finalGraph.txt")
    graph.fromFile(False)
    isNodeUnderMouse = False
    node1 = None
    node2 = None

    while (running):
        isNodeUnderMouse = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open(input("Where would you like to save the graph: "),"w")
                for i in graph.links:
                    file.write(i[0].text + " " + i[1].text + " " + str(i[2]) + " " + i[3] + "\n")
                file.close()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    find = input("Name of node: ")
                    for i in graph.nodes:
                        if i.text == find:
                            i.color = BLUE
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                for i in graph.nodes:
                    if(mouseX > i.pos[0] - i.radius and \
                            mouseY > i.pos[1] - i.radius and \
                            mouseX < i.pos[0] + i.radius and \
                            mouseY < i.pos[1] + i.radius):
                        graph.drawLinks(i)
                        if (node1):
                            node2 = i
                            description = input("Description of link: ")
                            if (description != "no"):
                                graph.links.append([node1, node2, 1.0, description])
                            node2 = None
                            node1 = None
                        elif (not node1 and not node2):
                            node1 = i
                        isNodeUnderMouse = True
                if (not isNodeUnderMouse):
                    newNode = Node(pos=(mouseX, mouseY), vel=(0,0), text = input("New node text: "))
                    graph.nodes.append(newNode)
                    node1 , node2 = (None, None)
        screen.fill(BLACK)

        graph.draw()
        mouseX, mouseY = pygame.mouse.get_pos()
        for i in graph.nodes:
            if(mouseX > i.pos[0] - i.radius and \
                            mouseY > i.pos[1] - i.radius and \
                            mouseX < i.pos[0] + i.radius and \
                            mouseY < i.pos[1] + i.radius):
                i.color = GREEN
                if (i not in graph.nodesUnderMouse):
                    graph.nodesUnderMouse.append(i)
                graph.drawLinks(i)
            else:
                if i in graph.nodesUnderMouse:
                    graph.nodesUnderMouse.remove(i)
                if (i.color != BLUE):
                    i.color = RED
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()
