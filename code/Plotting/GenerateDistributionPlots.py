import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sobol_seq
import chaospy as cp


def main():
    N=[50, 200, 500, 1000, 5000]
    rand2d  = None
    i=0;
    for n in N:
        #Generate X, #Generate Y
        df = pd.DataFrame({'x': np.random.uniform(0,1,n),
                           'N': np.repeat(n, n),
                           'Type': 'Uniform'})
        if rand2d is None:
            rand2d = df
        else:
            rand2d= rand2d.append(df)

        df = pd.DataFrame({'x': np.random.normal(0.5, 0.25, n),
                           'N': np.repeat(n, n),
                           'Type': 'Normal'})
        rand2d = rand2d.append(df)

        df = pd.DataFrame({'x': np.random.exponential(0.25, n),
                           'N': np.repeat(n, n),
                           'Type': 'Exponential'})
        rand2d = rand2d.append(df)



    g = sns.FacetGrid(rand2d, col='N', row='Type')
    g = g.map(sns.distplot, 'x', hist=False)
    plt.show()

    #Now Generate the QuasiRandom Plot
    rand2d = None
    for n in N:
        #Generate X, #Generate Y
        distribution = cp.Uniform(0, 1)
        df = pd.DataFrame({'x': distribution.sample(n, rule='S'),
                           'N': np.repeat(n, n),
                           'Type': 'Uniform'})
        if rand2d is None:
            rand2d = df
        else:
            rand2d= rand2d.append(df)

        distribution = cp.Normal(0.5, 0.25)
        df = pd.DataFrame({'x': distribution.sample(n, rule='S'),
                           'N': np.repeat(n, n),
                           'Type': 'Normal'})
        rand2d = rand2d.append(df)

        distribution = cp.Exponential(0.25,0)
        df = pd.DataFrame({'x': distribution.sample(n, rule='S'),
                           'N': np.repeat(n, n),
                           'Type': 'Exponential'})

        rand2d = rand2d.append(df)
    g = sns.FacetGrid(rand2d, col='N', row='Type')
    g = g.map(sns.distplot, 'x', hist=False)
    plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()
