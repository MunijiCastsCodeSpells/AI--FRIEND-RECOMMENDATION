import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph):

    plt.figure(figsize=(8,6))

    nx.draw(
        graph,
        node_size=50,
        node_color="lightblue",
        with_labels=False
    )

    plt.title("Social Network Graph")
    plt.show()