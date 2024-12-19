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

def add_edge(node_1, node_2, cost):
    adj[all_nodes.index(node_1), all_nodes.index(node_2)] = cost

# Construct the graph
add_edge('S', 'A', 3)
add_edge('S', 'D', 2)
add_edge('A', 'B', 5)
add_edge('A', 'C', 10)
add_edge('D', 'B', 1)
add_edge('D', 'E', 4)
add_edge('B', 'C', 2)
add_edge('B', 'E', 1)
add_edge('C', 'G', 4)
add_edge('E', 'G', 3)

print('Adjacency matrix:')
print(adj)

# Status of each node
visited = np.zeros((N))

# Parent
parent = np.zeros((N))
parent[:] = -1

# g(x) cost to reach each node
g_score = np.full(N, np.inf)
g_score[all_nodes.index(start_state)] = 0  # Start node has g(x) = 0


# A* Search
def A_Tree_Search(u):
    node_list = [u]
    visited[u] = 1
    while node_list:
        # Get the node with the lowest f(x) = g(x) + h(x)
        current = min(node_list, key=lambda node: g_score[node] + heuristic[all_nodes[node]])
        node_list.remove(current)
        # If goal state is reached, stop the search
        if all_nodes[current] == goal_state:
            return
        
        # Explore neighbors of current node
        for v in range(N):
            if adj[current, v] > 0:  # If there is a connection
                temp_g = g_score[current] + adj[current, v]
                
                # If the new path to neighbor is shorter
                if temp_g < g_score[v]:
                    parent[v] = current
                    g_score[v] = temp_g
                    if visited[v] == 0:
                        node_list.append(v)
                        visited[v] = 1
                        
                        
# Start A* Tree Search
A_Tree_Search(all_nodes.index('S'))

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
    print('Path:', path, 'Cost: ',g_score[all_nodes.index(goal_state)])
