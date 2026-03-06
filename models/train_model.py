import random
import pandas as pd
import networkx as nx
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def get_features(graph, u, v):
    common = len(list(nx.common_neighbors(graph, u, v)))
    neighbors_u = set(graph.neighbors(u))
    neighbors_v = set(graph.neighbors(v))

    union = neighbors_u.union(neighbors_v)
    if len(union) == 0:
        jaccard = 0
    else:
        jaccard = common /len(union)

    return common, jaccard

def train_ai_model(graph):
    data=[]
    nodes = list(graph.nodes())

    for _ in range(500):
        u= random.choice(nodes)
        v= random.choice(nodes)

        if u==v:
            continue

        common, jaccard= get_features(graph,u, v)

        label = 1 if graph.has_edge(u,v) else 0

        data.append([common, jaccard, label])
    df = pd.DataFrame(data, columns = ["common_neighbors","jaccard","label"])
    X= df[["common_neighbors","jaccard"]]
    Y = df["label"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train,Y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(Y_test, predictions)

    print("Model accuracy", accuracy)

    return model