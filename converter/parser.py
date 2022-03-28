import numpy as np
import pandas as pd


def parse(filename):
    L = pd.read_csv(filename, header=None, sep=',')
    table = np.array(L, np.int32)
    df = pd.DataFrame(data=table)
    return df

if __name__ == '__main__':
    f = parse('edge.dt3')
    #print(f)
