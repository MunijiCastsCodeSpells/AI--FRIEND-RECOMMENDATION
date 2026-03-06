from data.load_dataset import load_facebook_graph
from embeddings.node2vec_embeddings import gen_embeddings
from models.train_model import train_ai_model
from recommend.recommend_friends import recommend_friends
from visualise.network import visualize_graph
from visualise.embedding_plot import plot_embeddings

def main():

    graph = load_facebook_graph()

    model = train_ai_model(graph)
    node2vec_model = gen_embeddings(graph)
    user = 1

    recommendations = recommend_friends(graph,model,node2vec_model,user)
    print ("\nFriend recommendations for user", user)
    for r in recommendations:
        print ("User:",r[0], "Score:", r[1])

    visualize_graph(graph)    
    plot_embeddings(node2vec_model)

if __name__ == "__main__":
    main()
