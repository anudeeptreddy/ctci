def dfs(graph, order, node):
    node.visited = True
    for neighbor in node.adj_nodes:
        if not neighbor.visited:
            dfs(graph, order, neighbor)
    order.append(node)


def build_order(graph, nodes):
    order = []
    for node in nodes:
        if not graph[node].visited:
            dfs(graph, order, graph[node])
    order.reverse()
    return order


class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adj_nodes = []

    def add_adj_node(self, node):
        self.adj_nodes.append(node)


if __name__ == '__main__':
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    edges = [('f', 'c'), ('f', 'a'), ('f', 'b'), ('c', 'a'), ('b', 'a'), ('b', 'e'), ('a', 'e'), ('d', 'g')]
    # construct graph
    G = {node: Node(node) for node in nodes}
    for (source, dest) in edges:
        G[source].add_adj_node(G[dest])

    for key in G.keys():
        print G[key].data, ' '.join([str(node.data) for node in G[key].adj_nodes])

    order = build_order(G, nodes)
    print 'topological order:'
    for node in order:
        print node.data,


# o/p:
# a e
# c a
# b a e
# e
# d g
# g
# f c a b
# topoligical order:
# f d g c b a e