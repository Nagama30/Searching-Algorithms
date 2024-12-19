import numpy as np

# Set of nodes
all_nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'G']

# Heuristic values for each node (h(x))
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

# Adjacency matrix with edge weights (costs)
adj = np.zeros((N, N))

# Add edge with costs
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

# Parent of each node
parent = np.zeros((N))
parent[:] = -1

# Distance (g(x)) from start node
g = np.full(N, np.inf)
g[all_nodes.index(start_state)] = 0

# A* Graph Search
def A_Graph_Search(start):
    INF = 1e9
    g[:] = INF
    g[start] = 0
    
    while True:
        u = -1
        smallest_f = INF
        # Select the node with the smallest f(x) = g(x) + h(x)
        for v in range(N):
            if visited[v] == 0 and g[v] + heuristic[all_nodes[v]] < smallest_f:
                u = v
                smallest_f = g[v] + heuristic[all_nodes[v]]
        
        if u == -1:
            break

        visited[u] = 1
        # Check if we have reached the goal
        if all_nodes[u] == goal_state:
            return

        # Explore all neighbors of u
        for v in range(N):
            if adj[u, v] != 0 and visited[v] == 0:
                tentative_g = g[u] + adj[u, v]
                # Update g(v) and parent if a better path is found
                if tentative_g < g[v]:
                    g[v] = tentative_g
                    parent[v] = u

# Start A* Graph Search from start_state
A_Graph_Search(all_nodes.index(start_state))

# Check if goal state (G) is reached
if visited[all_nodes.index(goal_state)] == 0:
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
    print('Path:', path, 'Cost: ',g[all_nodes.index(goal_state)])
