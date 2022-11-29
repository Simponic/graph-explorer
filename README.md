# Graph Explorer
This is a WOK (wealth of knowledge) explorer that I made as a fun project for CSE280.

https://user-images.githubusercontent.com/25559600/204606705-ea742b05-b452-47e0-9069-b7cc5e7339a6.mp4


## Installation

All you need is pygame!

```bash
pip install pygame
```

## Usage
For a video overview: watch on (YouTube)[https://www.youtube.com/watch?v=nIgWwrd05ts]

```bash
cd src
python3 main.py
```
Select a node by clicking it; this will focus the links that are directed out of that node.

Press "P" to select all nodes.

Press "F" to find a node (this is done as a prompt in the shell).

Press "Space" to pause the visualization.

Press "C" to clear all the selected nodes.


## Using the WOK Builder

```bash
cd src
python3 builder.py
```

The builder is a simple one; click anywhere where there is not a node to create a new one (prompted in terminal).

You can add links between nodes by selecting first the source node and then the directed node. A description for the link will be prompted in the terminal.

If you accidentally link two nodes, you can cancel the link by typing "no" in the description.

Press "F" to search for a node. If found, this node will turn blue.
