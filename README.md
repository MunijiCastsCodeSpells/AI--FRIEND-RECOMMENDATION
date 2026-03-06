# AI Friend Recommendation System using Graph Embeddings

This project implements an **AI-powered friend recommendation system** using graph theory, machine learning, and node embeddings.

The system analyzes a social network graph and predicts potential friendships using link prediction techniques and graph representation learning.

---

## Project Overview

Social media platforms recommend new connections by analyzing the structure of their social networks.  

This project builds a simplified version of such a system using:

- Graph-based features
- Machine learning models
- Node embeddings

The model predicts the likelihood that two users will form a connection in the future.

---

## Features

- Load and process real social network data
- Extract graph-based features
- Train a machine learning model for link prediction
- Generate graph embeddings using Node2Vec
- Recommend new friends based on similarity and predictions
- Visualize the embedding space

---

## Dataset

This project uses the **Facebook Social Circles dataset** from the Stanford Network Analysis Project (SNAP).

Dataset: https://snap.stanford.edu/data/facebook_combined.txt.gz

Dataset statistics:

- ~4039 users
- ~88,000 friendships

---

## Technologies Used

- Python
- NetworkX
- Scikit-learn
- Node2Vec
- Pandas
- Matplotlib

---

## Machine Learning Approach

The recommendation system uses **link prediction** techniques.

Features used for prediction:

- Number of common neighbors
- Jaccard similarity

A **Logistic Regression** model is trained to predict the probability of friendship between two users.

---

## Graph Embeddings

The project uses **Node2Vec** to learn vector representations of users in the network.

These embeddings capture:

- community structure
- structural similarity
- connectivity patterns

Users with similar embeddings are likely to belong to the same social group.
