import sys

# Constants for the knight's movement
DX = [1, 2, 2, 1, -1, -2, -2, -1]
DY = [-2, -1, 1, 2, 2, 1, -1, -2]

def output_label(label, n):
    """Output the current labeling of the board."""
    for j in range(n):
        print(label[0][j], end="")
        for i in range(1, n):
            print(" ", label[i][j], end="")
        print()

def output(label, n):
    """Output the solution and write to Solution.txt."""
    print("Solution:")
    output_label(label, n)
    
    # Write solution to a file
    with open("Solution.txt", "w") as f:
        f.write(f"{n}\n")
        for j in range(n):
            f.write(f"{label[0][j]}")
            for i in range(1, n):
                f.write(f" {label[i][j]}")
            f.write("\n")

    sys.exit(0)

def init(deg, n):
    """Initialize the degree matrix."""
    for i in range(n):
        for j in range(n):
            for t in range(8):
                u = i + DX[t]
                v = j + DY[t]
                if 0 <= u < n and 0 <= v < n:
                    deg[i][j] += 1

def BackTracking(number, i, j, label, deg, n):
    """Backtracking function to find a knight's tour."""
    label[i][j] = number
    
    if number < n * n:
        nChoices = 0
        d = []
        next_moves = []

        for t in range(8):
            u = i + DX[t]
            v = j + DY[t]
            if 0 <= u < n and 0 <= v < n and label[u][v] == 0:
                d.append(deg[u][v])
                next_moves.append(t)
                nChoices += 1
                deg[u][v] -= 1

        # Sort next_moves based on their degree
        for u in range(nChoices):
            for v in range(u + 1, nChoices):
                if d[u] > d[v]:
                    d[u], d[v] = d[v], d[u]
                    next_moves[u], next_moves[v] = next_moves[v], next_moves[u]

        # Explore each possible next move
        for t in range(nChoices):
            BackTracking(number + 1, i + DX[next_moves[t]], j + DY[next_moves[t]], label, deg, n)
        
        # Restore the degree counts
        for t in range(8):
            u = i + DX[t]
            v = j + DY[t]
            if 0 <= u < n and 0 <= v < n and label[u][v] == 0:
                deg[u][v] += 1
    else:
        output(label, n)  # If the tour is complete, output the result
    
    label[i][j] = 0  # Backtrack

def knight_tour(N, start_x, start_y):
    """Main function to initiate the knight's tour from a given starting position."""
    label = [[0 for _ in range(N)] for _ in range(N)]
    deg = [[0 for _ in range(N)] for _ in range(N)]
    init(deg, N)  # Initialize the degree matrix
    BackTracking(1, start_x - 1, start_y - 1, label, deg, N) 
    
    
# Example usage
N = 6 # Size of the chessboard
start_x = 1  # Starting row (1-indexed)
start_y = 1  # Starting column (1-indexed)
knight_tour(N, start_x, start_y)  # Call the knight_tour function
