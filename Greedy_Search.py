import numpy as np

# Set of nodes
all_nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'G']

# Heuristic values for each node
heuristic = {
    'S': 7,
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0
}

# Start state
start_state = 'S'

# Goal state
goal_state = 'G'

# Number of nodes
N = len(all_nodes)

# Adjacency matrix
adj = np.zeros((N, N))

def add_edge(node_1, node_2):
    adj[all_nodes.index(node_1), all_nodes.index(node_2)] = 1

# Construct the graph
add_edge('S', 'A')
add_edge('S', 'D')
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('D', 'B')
add_edge('D', 'E')
add_edge('B', 'C')
add_edge('B', 'E')
add_edge('C', 'G')
add_edge('E', 'G')

print('Adjacency matrix:')
print(adj)

# Status of each node
visited = np.zeros((N))

# Parent
parent = np.zeros((N))
parent[:] = -1

# Greedy Search
def Greedy_Search(u):
    visited[u] = 1
    while True:
        # Get the nodes to which direct connection exists from current node
        nodes_from_u = []
        for v in range(N):
            if adj[u, v] == 1 and visited[v] == 0:
                nodes_from_u.append(v)
               
        # If there are no direct nodes, break the loop
        if len(nodes_from_u) == 0:
            break
        
        # Find the node with the smallest heuristic value
        best_node = nodes_from_u[0]
        for v in nodes_from_u:
            if heuristic[all_nodes[v]] < heuristic[all_nodes[best_node]]:
                best_node = v
        
        # Mark the best node as visited and set its parent
        visited[best_node] = 1
        parent[best_node] = u
        
        # If the goal is reached, stop the search
        if all_nodes[best_node] == goal_state:
            return

        # Move to the best node
        u = best_node

# Start Greedy Search
Greedy_Search(all_nodes.index('S'))

# Check if the goal was reached
if visited[all_nodes.index('G')] == 0:
    print('There is no path from S to G')
else:
    print('There is at least a path from S to G')
    # Reconstruct the path from start to goal
    path = []
    i = all_nodes.index('G')
    while i != -1:
        path.append(i)
        i = int(parent[i])
    path.reverse()
    # Convert path indices to node names
    path = [all_nodes[element] for element in path]
    print('Path:', path)
