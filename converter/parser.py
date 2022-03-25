import csv
import numpy as np
import pandas as pd


def parse(filename):

    row = pd.read_csv(filename, header=None, sep=':')

    x, y = row.iloc[0][0].split(',')
    x = int(x)
    y = int(y)

    l = row.iloc[0][1].split(',')
    L = list()
    for i in range(y):
        if i == 0:
            start = 0
        else:
            start = i * x
        last = (i+1) * x
        L.append(l[start:last])
    
    table = np.array(L, np.int32)
    df = pd.DataFrame(data=table)
    return df

if __name__ == '__main__':
    f = parse('edge.dt3')
    #print(f)
