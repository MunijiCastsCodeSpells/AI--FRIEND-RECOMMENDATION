from node2vec import Node2Vec

def gen_embeddings(graph):
    node2vec = Node2Vec(graph,dimensions=32,walk_length = 10, num_walks =50, workers =3)

    model = node2vec.fit(window=5,min_count =1)
    return model
