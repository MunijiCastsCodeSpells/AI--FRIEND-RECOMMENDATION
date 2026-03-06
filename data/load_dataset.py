import networkx as nx

def load_facebook_graph():
    path = "dataset/facebook_combined.txt"
    G = nx.read_edgelist(path, nodetype=int)

    print("Dataset loaded")
    print("Users:", G.number_of_nodes())
    print("Friendships:", G.number_of_edges())

    return G