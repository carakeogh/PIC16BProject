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
from io import BytesIO
import base64


def start():
    """
    This function prepares the image data. It returns an image path and the image files.
    """

    ### SET 'imgs_path' TO YOUR LOCAL MACHINE'S ABSOLUTE PATH to 'images' folder within 'data' directory ###
    imgs_path = "C:/Users/wangp/OneDrive/Documents/GitHub/PIC16BProject/data/images/"

    files = [imgs_path + x for x in os.listdir(imgs_path) if "jpg" in x]

    # In order to reduce compilation/training time of algorithm, we reduce the data to 500 images
    files = files[0:500]

    return imgs_path, files


from keras import models

def model(file):
    """
    This function applies the outfit recommender model to the file.

    argument:
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
        image_batch = np.expand_dims(numpy_image, axis = 0)  
        
        importedImages.append(image_batch)
    
    images = np.vstack(importedImages)

    # prepare the image for the VGG model
    processed_imgs = preprocess_input(images.copy()) 

    # predict all the data
    img_features = model.predict(processed_imgs) 
 
    return img_features


def recommended_outfit(data, img):
    """
    This function retrieves the 5 most similar products to the user-selected image.

    arguments:
    data: stored data of model predictions from 'model()' function
    img: image that is going to be used to find its most similar products

    return: a list of the closest 5 images
    """
    
    # now find the cosine similarities between each images
    cosSimilarities = cosine_similarity(data) 
    # store the results into a pandas dataframe 
    cos_similarities_df = pd.DataFrame(cosSimilarities, columns = start()[1], index = start()[1])  
    

    # get the five closest images
    closest_imgs = cos_similarities_df[img].sort_values(ascending = False)[1:6].index

    storage = []

    # store the five closest images into storage
    for i in range(len(closest_imgs)):
        original = load_img(closest_imgs[i], target_size = (224, 224))
        storage.append(original)

    return storage


def plot(x):
    """
    This function plots the images so that the user can see them on the similar_products webpage

    argument:
    x: the list of matplotlib images from recommended_outfit function

    return:
    a list of image urls for each similar product to pass into html file 
    """
    store = []

    for i in x:
        # converts matplotlib figure into png image for html
        fig = plt.figure()
        img = BytesIO()
        fig.savefig(img, format = 'png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue())
        html = '<img src="data:image/png;base64, {}">'.format(plot_url.decode('utf-8'))


        store.append(html)
    
    return store
