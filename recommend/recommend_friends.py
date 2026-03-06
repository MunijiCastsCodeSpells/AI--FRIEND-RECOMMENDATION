import networkx as nx
import pandas as pd

def recommend_friends(graph, model, node2vec_model, user, top_n=5):

    recommendations = []

    for node in graph.nodes():

        if node == user:
            continue

        if graph.has_edge(user, node):
            continue

        # Graph features
        common = len(list(nx.common_neighbors(graph, user, node)))

        neighbors_u = set(graph.neighbors(user))
        neighbors_v = set(graph.neighbors(node))

        union = neighbors_u.union(neighbors_v)

        jaccard = common / len(union) if len(union) > 0 else 0

        features = pd.DataFrame([[common, jaccard]],columns=["common_neighbors", "jaccard"])


        # Embedding similarity
        similarity = node2vec_model.wv.similarity(str(user), str(node))

        # ML prediction
        probability = model.predict_proba(features)[0][1]

        score = probability + similarity

        recommendations.append((node, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:top_n]