# Function to insert vertices
# to adjacency list
def insert(adj, u, v):
    # Insert a vertex v to vertex u
    adj[u].append(v)
    return


# Function to display adjacency list
def printlist(adj, vert):
    for i in range(vert):
        print(i, end='')

        for j in adj[i]:
            print(' --> ' + str(j), end='')

        print()

    print()


# Function to convert adjacency
# list to adjacency matrix
def convert(adj, vert):
    # Initialize a matrix
    matrix = [[0 for j in range(vert)]
              for i in range(vert)]

    for i in range(vert):
        for j in adj[i]:
            matrix[i][j] = 1

    return matrix


# Function to display adjacency matrix
def printmatrix(adj, v):
    for i in range(v):
        for j in range(v):
            print(adj[i][j], end=' ')

        print()

    print()


# Driver code
if __name__ == '__main__':
    V = 5

    adjList = [[] for i in range(V)]

    # Inserting edges
    insert(adjList, 0, 1)
    insert(adjList, 0, 4)
    insert(adjList, 1, 0)
    insert(adjList, 1, 2)
    insert(adjList, 1, 3)
    insert(adjList, 1, 4)
    insert(adjList, 2, 1)
    insert(adjList, 2, 3)
    insert(adjList, 3, 1)
    insert(adjList, 3, 2)
    insert(adjList, 3, 4)
    insert(adjList, 4, 0)
    insert(adjList, 4, 1)
    insert(adjList, 4, 3)

    # Display adjacency list
    print("Adjacency List: ")
    printlist(adjList, V)

    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(adjList, V)

    # Display adjacency matrix
    print("Adjacency Matrix: ")
    printmatrix(adjMatrix, V)
