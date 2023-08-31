import numpy as np
from sklearn.cluster import KMeans
customer_data = np.array([
    [35, 75000, 2, 75, 4.5, 60],
    [28, 60000, 0, 120, 4.2, 45],
    [45, 85000, 3, 95, 4.8, 90],
    [32, 55000, 1, 60, 4.0, 30],
    [40, 90000, 2, 80, 4.6, 75]
])
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(customer_data)
cluster_labels = kmeans.labels_
new_customer_features = np.array([
    float(input("Enter age: ")),
    float(input("Enter income: ")),
    float(input("Enter number of children: ")),
    float(input("Enter average transaction amount: ")),
    float(input("Enter product reviews: ")),
    float(input("Enter time spent shopping: "))
])
predicted_cluster = kmeans.predict([new_customer_features])
print("Predicted cluster for the new customer:", predicted_cluster[0])
