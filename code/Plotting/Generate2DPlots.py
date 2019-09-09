import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sobol_seq



def main():
    N=[2, 10, 15, 25,50]
    rand2d  = None
    i=0;
    for n in N:
        #Generate X, #Generate Y
        df = pd.DataFrame({'x': 10 * np.random.uniform(0,1,n),
                           'y': 10 * np.random.uniform(0,1,n),
                           'N': np.repeat(n, n),
                           'Type': 'random'})
        if rand2d is None:
            rand2d = df
        else:
            rand2d= rand2d.append(df)

        quasi = sobol_seq.i4_sobol_generate(2, n).transpose()
        df = pd.DataFrame({'x': 10 * quasi[0],
                           'y': 10 * quasi[1],
                           'N': np.repeat(n, n),
                           'Type': 'Quasirandom'})

        rand2d = rand2d.append(df)

    g = sns.FacetGrid(rand2d, col='N', row='Type')
    g = g.map(plt.scatter, 'x', 'y')
    plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()
