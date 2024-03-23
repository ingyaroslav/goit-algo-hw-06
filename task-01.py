import networkx as nx
import matplotlib.pyplot as plt

# Створення графа транспортної мережі міста
G = nx.random_geometric_graph(20, 0.3)

# Візуалізація графа
pos = nx.spring_layout(G)  # позиціонування вершин
nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue')
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

# Ступінь вершин
degrees = [val for (node, val) in G.degree()]
print("Максимальний ступінь вершин:", max(degrees))
print("Середній ступінь вершин:", sum(degrees) / len(degrees))
