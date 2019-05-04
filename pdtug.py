import pandas as pd
import numpy as np
import sys

def pdtug(df, k):

    graph = {}
    dist_df = pd.DataFrame(pd.np.empty((len(df), 0)) * pd.np.nan)

    for i in range(0,len(df)):

        dist_df['dist'+str(i)] = sys.float_info.max

        actual = df.values[i]

        for j in range(0,len(df)):
            if(i != j):
                dist_df['dist'+str(i)].values[j] = np.linalg.norm(actual-df.values[j])

        dist_df = dist_df.sort_values('dist'+str(i))
        graph[i] = list(dist_df['dist'+str(i)].index[0:k])

    for i in range(0,len(df)):
        graph[i] += ([k for k,v in graph.items() if i in v])
        graph[i] = list(set(graph[i]))

    return graph