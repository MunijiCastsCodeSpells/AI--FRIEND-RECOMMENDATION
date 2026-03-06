import networkx as nx
def generate_graph(users=100, connections = 3):
    G = nx.barabasi_albert_graph(users,connections)

    print("generated network")
    print("users:", G.number_of_nodes())
    print("friendships", G.number_of_edges())

    return G