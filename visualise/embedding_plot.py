import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def plot_embeddings(model):

    nodes = list(model.wv.index_to_key)

    embeddings = [model.wv[node] for node in nodes]

    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)

    xs = reduced[:,0]
    ys = reduced[:,1]

    plt.figure(figsize=(8,6))
    plt.scatter(xs, ys, s=10)

    plt.title("Node2Vec Embedding Visualization")
    plt.show()