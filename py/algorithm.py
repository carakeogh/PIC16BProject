from PIL import Image
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import tensorflow as tf

from keras.applications import vgg16
from keras.preprocessing.image import load_img,img_to_array, ImageDataGenerator
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input
from keras import layers, optimizers, utils
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
matplotlib.use('Agg')
from io import BytesIO
import base64

def start():
    """
    prepare our image data
    """
    imgs_path = "data/images"
    files = [imgs_path + x for x in os.listdir(imgs_path) if "jpg" in x]
    # In order to reduce compilation time of the algorithm, we reduce the data to 500 images
    files = files[0:500]

    return imgs_path, files

from keras import models

def model(file):
    """
    apply our outfit recommender model to file

    arguement:
    file: image data

    return: a dataframe containing information of the cosine similarity score of each image data
    """
    # we use vgg16 model to process image identification
    vgg_model = vgg16.VGG16(weights='imagenet')
    # remove the last layers in order to get features instead of predictions
    model = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)

    # now we run all 500 images we extracted through model
    importedImages = []
    # since vgg16 can only process one image at a time, we use for loop to loop through all images
    for f in file:
        filename = f
        # vgg16 only accept images with size 224x224
        original = load_img(filename, target_size = (224, 224))
        numpy_image = img_to_array(original)  
        # convert the image into batch format
        image_batch = np.expand_dims(numpy_image, axis=0)  
        
        importedImages.append(image_batch)
    
    images = np.vstack(importedImages)

    # prepare the image for the VGG model
    processed_imgs = preprocess_input(images.copy()) 

    # predict all the data
    img_features = model.predict(processed_imgs) 

    # now find the cosine similarities between each images
    cosSimilarities = cosine_similarity(img_features) 
    # store the results into a pandas dataframe 
    cos_similarities_df = pd.DataFrame(cosSimilarities, columns = file, index = file)  
 
    return cos_similarities_df

def recommended_outfit(img, df):
    """
    retrieve the most similar 5 products for the inputted image

    arguements:
    img: image that is going to be used to find its most similar products

    return: a list of the closest 5 images
    """

    # get the five closest images
    closest_imgs = df[img].sort_values(ascending = False)[1:6].index

    storage = []

    # store the five closest images into storage
    for i in range(len(closest_imgs)):
        original = load_img(closest_imgs[i], target_size = (224, 224))
        storage.append(original)

    return storage

def plot(x):
    store = []

    for i in x:
        img = BytesIO()
        y = [1,2,3,4,5]
        x = [0,2,1,3,4]

        plt.plot(x,y)

        plt.savefig(img, format = 'png')
        plt.close()
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        store.append(plot_url)
    
    return store
