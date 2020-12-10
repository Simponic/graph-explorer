from globals import *
from Node import Node

def findNode(node, listOfNodes):
    for i in range(len(listOfNodes)):
        if node.text == listOfNodes[i].text:
            return i
    return len(listOfNodes)

# Each file is in the form
# <source> <destination> <weight>
def parse_input(filename):
    nodes = []
    links = []

    lines = open(filename, "r").readlines()

    for line in lines:
        # Parse each line and add to links array
        if (not line == "\n"): # Line isn't empty
            line_split = line.split(" ")
            currSrc = Node(text=line_split[0])
            currDest = Node(text=line_split[1])

            currSrc_index, currDest_index = (findNode(currSrc, nodes), findNode(currDest, nodes))
            appendSrc, appendDest = (False, False)
            if (currSrc_index == len(nodes)):
                appendSrc = True
            if (currDest_index == len(nodes)):
                appendDest = True
            if (appendSrc):
                nodes.append(currSrc)
                currSrc_index = len(nodes)-1
            if (appendDest):
                nodes.append(currDest)
                currDest_index = len(nodes)-1

            if (len(line_split) > 2):
                connection_description = "".join([str(x).strip() + " " for x in line_split[3::]])
            else:
                connection_description = ""
            # Append the connection to links
            links.append((nodes[currSrc_index], nodes[currDest_index], float(line_split[2]), connection_description))

    return [nodes, links]

