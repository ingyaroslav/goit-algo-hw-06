import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Задання графа
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('D', 'E', 7)

# Додамо ребра, що з'єднують вершину 'E' з усіма іншими вершинами з нульовою вагою
for vertex in list(graph.graph.keys()):  # Використовуємо list() для створення копії списку ключів
    if vertex != 'E':
        graph.add_edge('E', vertex, 0)

# Запускаємо алгоритм Дейкстри для знаходження найкоротших відстаней від вершини 'A'
start_vertex = 'A'
shortest_distances = graph.dijkstra(start_vertex)
print("Найкоротший шлях від вершини", start_vertex)
for vertex, distance in shortest_distances.items():
    print("Вершина:", vertex, ", Відстань:", distance)
