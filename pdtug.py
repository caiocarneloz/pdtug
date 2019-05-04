import pandas as pd
import numpy as np

def pdtug(df, k):

    graph = {}
    
    for i in range(0,len(df)):

        dist = [float("inf")] * len(df)

        actual = df.values[i]

        for j in range(0,len(df)):
            if(i != j):
                dist[j] = np.linalg.norm(actual-df.values[j])

        dist = np.array(dist)
        dist = np.argsort(dist)
        graph[i] = list(dist[0:k])

    for i in range(0,len(df)):
        graph[i] += ([k for k,v in graph.items() if i in v])
        graph[i] = list(set(graph[i]))

    return graph