import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Remember this method gets executed first since its our 'main'
def main(data):

    #Reading in data
    df = pd.read_csv(data)
    print(df.shape)
    #Lets filter the data so we are only looking at the midnight audit
    df = df[df.Time == '00:00:00']
    print(df.shape)

    print("Plotting the number of Turnstiles per station")
    count_per_station = df.groupby('Station')['SCP'].nunique()


    StationCount= df['Station'].nunique()
    print("Num Unique Stations:{}".format(StationCount))

    TurnstileCount= count_per_station.sum()


    print("Num Turnstiles: {}".format(TurnstileCount))

    print("Avg Number of Turnstiles per Station={}".format(TurnstileCount/StationCount))

    print("Avg Number of Entries per Turnstile={}".format(df['Entries'].mean()))

    # An "interface" to matplotlib.axes.Axes.hist() method
    n, bins, patches = plt.hist(x=count_per_station, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Turnstile Count')
    plt.ylabel('Frequency')
    plt.title('Turnstile Count Per Station')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.show()







if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lets munge some data')
    parser.add_argument('--data', dest='data', required=False,
                        default='../../data/Turnstile_Usage_Data_2018_Sample.csv',
                        help='where is the data csv located?')

    args = parser.parse_args()
    main(args.data)