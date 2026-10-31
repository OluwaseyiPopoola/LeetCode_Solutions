"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
        
        explored = set()
        created = {}

        def connect_node(node_a: Node, node_b: Node):
            node_a.neighbors.append(node_b)
            node_b.neighbors.append(node_a)

        def copy_graph(node: Node, newNode: Node):
            
            new_neighbors = []
            explored.add(node)

            for neigh_node in node.neighbors:
                if neigh_node in explored:
                    continue
                
                new_neigh_node = Node(neigh_node.val) if neigh_node not in created else created[neigh_node]
                created[neigh_node] = new_neigh_node
                connect_node(newNode, new_neigh_node)
                new_neighbors.append((neigh_node, new_neigh_node))
            
            # print(f"Node({node.val})")
            # print([f"({node.val}), ({neigh_node.val})" for node, neigh_node in new_neighbors])
            # print()

            for neigh_node, new_neigh_node in new_neighbors:
                copy_graph(neigh_node, new_neigh_node)

        newNode = Node(node.val)
        created[node] = newNode
        copy_graph(node, newNode)

        return newNode
        