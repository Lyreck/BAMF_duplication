## L'idée: 

#1- compute levenshtein between everybody
#2- create clusters based on closest proximity (can be a threshold, can be a kmeans*, hierarchical clustering, or DBSCAN - or approximate nearest neighbours)
#3- display these clusters in a graph for case workers to visualize.

#* k-means is only with euclidean distances. I'll try with DBSCAN (see F.Sur and https://scikit-learn.org/0.16/faq.html#how-do-i-deal-with-string-data-or-trees-graphs)

# For more brainstorming about this, see this discussion with Mistral https://chat.mistral.ai/chat/15cf95e3-69d0-4c41-b7db-13efd6452ea2.

from sklearn.cluster import DBSCAN
from sklearn.metrics import pairwise_distances
from Levenshtein import distance
import pandas as pd
import numpy as np

# Sample data
data = pd.DataFrame({
    'name': ['John', 'Jon', 'Catherine', 'Kathryn'],
    'surname': ['Doe', 'Doe', 'Smith', 'Smyth'],
    'city': ['NY', 'NY', 'LA', 'LA'],
    'age': [30, 31, 25, 26]
})

# Compute similarity (example: Levenshtein for names, exact for city)
name_sim = pairwise_distances(data['name'], metric=lambda x, y: distance(x, y)) #reminder: distance is levenshtein distance here.
surname_sim = pairwise_distances(data['surname'], metric=lambda x, y: distance(x, y))
city_sim = pairwise_distances(data['city'], metric=lambda x, y: distance(x, y)) #account for minor typos in city names. But generally, if same city then same city.
#for age: we can use a simple euclidean distance, BUT more than 5 year difference shuold not change anything - I mean bigger than 5y it's just not the same person.

# Combine scores (weighted)
total_sim = 0.5*name_sim + 0.3*surname_sim + 0.2*city_sim #weight scores by importance. For example: For example:
# Name similarity: 50% weight
# Surname similarity: 30% weight
# City similarity: 15% weight
# Age similarity: 5% weight

# Cluster with DBSCAN
clusters = DBSCAN(eps=0.5, min_samples=2, metric='precomputed').fit(total_sim) #start with small eps

labels = clusters.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)

# ## Evaluation of the clusterization - see https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html for details.
# ## Only available if e have the 'true' labels. 
# from sklearn import metrics
# print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
# print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
# print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
# print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
# print(
#     "Adjusted Mutual Information:"
#     f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
# )
# print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")
import matplotlib.pyplot as plt
X = total_sim

unique_labels = set(labels)
core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[clusters.core_sample_indices_] = True

colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title(f"Estimated number of clusters: {n_clusters_}")
plt.show()



## OK LA SUITE: créer un joli graph avec javascriiiiiptttt hihi.

## Build a list of nodes
nodes = data["name"].values

## Build the list of edges: nodes are connected if and only if they are in the same cluster.
print(clusters.labels_)

dic={}

dic = {node: label} for node,label in zip(nodes, clusters.labels_)
for label,node in zip(clusters.labels_, nodes):
nod

    

## Represent the graph using networks

## Represent the graph using d3.js

