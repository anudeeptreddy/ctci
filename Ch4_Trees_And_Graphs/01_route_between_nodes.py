import Queue


def breadth_first_search(adj, source, target):
    queue = Queue.Queue()
    visited = [False] * len(adj)  # Track if a node is already visited
    queue.put(source)             # start BFS from source node
    while not queue.empty():      # While target is yet to find or undiscovered nodes exist
        node = queue.get()
        visited[node] = True            # mark node as visited
        for neighbor in adj[node]:      # explore all the unvisited neighbor nodes
            if not visited[neighbor]:
                if neighbor == target:  # target reached
                    return True
                else:
                    queue.put(neighbor)

    return False    # path don't exist to target node


if __name__ == '__main__':
    nodes = 5
    source, target = 0, 3
    edges = [(0, 1), (1, 4), (4, 0), (4, 2), (4, 3), (2, 3)]
    adj = [[] for _ in range(nodes)]  # Adjacency list
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    print(breadth_first_search(adj, source, target))