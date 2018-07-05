import os
import pandas as pd


def run():
    df = pd.read_csv(os.getenv('DATA_FILE', 'properties.csv'))
    print(df.head())


if __name__ == '__main__':
    run()
