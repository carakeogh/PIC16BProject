import pandas as pd
import random

def getData(type1):
    ''' 
    Function that merges styles.csv and images.csv together 
    and returns a new data frame for a certain clothing type
    '''
    df = pd.read_csv("styles.csv", nrows = 10000, error_bad_lines = False)
    image_df = pd.read_csv("images.csv")
    df['filename'] = df.apply(lambda row: str(row['id']) + ".jpg", axis = 1)

    # merge images.csv and styles.csv together
    df = pd.merge(df, image_df, on = ["filename"])
    df = df.sample(frac = 1).reset_index(drop = True)

    return df[df['subCategory'] == type1]


def randomSelect(df, k):
    '''
    Randomly select k items from a data frame 
    '''
    return random.sample(set(df["link"]), k)

