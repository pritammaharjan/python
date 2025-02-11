# -*- coding: utf-8 -*-
"""6996_path_finding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xeo47IxXD55JSukTw0jLFnEgjcm2u55g

Import the libraries
"""

import numpy as np
from google.colab import drive
drive.mount('/content/gdrive')

"""Import map.txt file from google drive"""

maze=np.loadtxt('/content/gdrive/My Drive/Colab Notebooks/6996_map.txt', delimiter= ',', dtype=int)
print(maze)

print(maze.shape) #to print out shape of the map

print(maze.size) #to print out the size of the map

class Node():
    "A* Pathfinding" # using A star algoalgorithm 

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.a = 0
        self.b = 0
        self.c = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    

    # the start node and end node
    start_node = Node(None, start)
    start_node.a = start_node.b = start_node.c = 0
    end_node = Node(None, end)
    end_node.a = end_node.b = end_node.c = 0

    
    open_list = [] #initialized open list
    closed_list = [] #initialized close list

    
    open_list.append(start_node) #input the start mode

    while len(open_list) > 0: #continue loop until the end node

        
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.c < current_node.c:
                current_node = item
                current_index = index

      
        open_list.pop(current_index)
        closed_list.append(current_node)

        # output the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return the path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the a, b, and c values
            child.a = current_node.a + 1
            child.b = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.c = child.a + child.b

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.a > open_node.a:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    start = (4, 9)#starting of the map
    end = (9, 5) #ending of the map

    path = astar(maze, start, end)
    print(path)
    


if __name__ == '__main__':
    main()

