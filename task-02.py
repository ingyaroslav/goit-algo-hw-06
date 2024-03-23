import networkx as nx

# Функція для знаходження шляхів за допомогою DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Функція для знаходження шляхів за допомогою BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Граф, створений у першому завданні
G = nx.random_geometric_graph(20, 0.3)

# Визначення початкової та кінцевої вершин
start = 0
goal = 19

# Знаходження шляхів за допомогою DFS
dfs_paths_result = list(dfs_paths(G, start, goal))
print("Шляхи за допомогою DFS:", dfs_paths_result)

# Знаходження шляхів за допомогою BFS
bfs_paths_result = list(bfs_paths(G, start, goal))
print("Шляхи за допомогою BFS:", bfs_paths_result)
