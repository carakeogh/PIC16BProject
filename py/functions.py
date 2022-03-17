import pandas as pd
import random

def getData(type1):
    """
    Function that merges styles.csv and images.csv together 
    and returns a new data frame for a certain clothing type

    argument:
    type1: the certain clothing type we want the dataframe to focus on

    return:
    the cleaned dataframe focussing on type1
    """ 

    # read in data
    df = pd.read_csv("data/styles.csv", nrows = 10000, error_bad_lines = False)
    image_df = pd.read_csv("data/images.csv")
    df['filename'] = df.apply(lambda row: str(row['id']) + ".jpg", axis = 1)

    # merge images.csv and styles.csv together
    df = pd.merge(df, image_df, on = ["filename"])
    df = df.sample(frac = 1).reset_index(drop = True)

    return df[df['subCategory'] == type1]


def randomSelect(df, k):
    """
    Randomly select k items from a data frame.

    arguments:
    df: dataframe of images in user-chosen category
    k: number of random items to select

    return: set of links to k number of random images
    """

    return random.sample(set(df["link"]), k)


def match(link):
    """
    Function that takes the link of the image and return its corresponding filename.

    argument:
    link: image link from randomSelect function

    return: filename of image as a string
    """
    
    # read in data
    df = pd.read_csv("data/styles.csv", nrows = 10000, error_bad_lines = False)
    image_df = pd.read_csv("data/images.csv")
    df['filename'] = df.apply(lambda row: str(row['id']) + ".jpg", axis = 1)

    # merge images.csv and styles.csv together
    df = pd.merge(df, image_df, on = ["filename"])
    df = df.sample(frac = 1).reset_index(drop = True)

    # find the corresponding filename given the link
    a = df[df['link'] == link]['filename']
    # convert our result to a
    a = str(a)
    # extract the filename as a string
    a = " ".join(a.split()[1:-4])

    return a


