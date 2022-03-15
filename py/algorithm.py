from PIL import Image
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import tensorflow as tf
import json
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
    imgs_path = "data/images"

    files = [imgs_path + x for x in os.listdir(imgs_path) if "jpg" in x]
    # In order to reduce compilation time of the algorithm, we reduce the data to 500 images
    files = files[0:500]

    return imgs_path, files

from keras import models

def model(file):
    # introduction of the model: https://medium.com/@mygreatlearning/what-is-vgg16-introduction-to-vgg16-f2d63849f615
    vgg_model = vgg16.VGG16(weights='imagenet')
    # # remove the last layers in order to get features instead of predictions
    model = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)

    # now we run all 500 images we extracted through model
    importedImages = []

    for f in file:
        filename = f
        original = load_img(filename, target_size = (224, 224))
        numpy_image = img_to_array(original)  # since vgg16 can only process one image at a time, we train the model with 'original' first
        image_batch = np.expand_dims(numpy_image, axis=0)  # convert the image / images into batch format
    
        importedImages.append(image_batch)
    
    images = np.vstack(importedImages)

    processed_imgs = preprocess_input(images.copy()) # prepare the image for the VGG model

    img_features = model.predict(processed_imgs) # predict training data

    # now find the cosine similarities between each images
    cosSimilarities = cosine_similarity(img_features)  
    cos_similarities_df = pd.DataFrame(cosSimilarities, columns = file, index = file)  # store the results into a pandas dataframe
 
    return cos_similarities_df

def recommended_outfit(img, df):
  """
  retrieve the most similar 5 products for the imputted image

  arguements:
  img: image that is going to be used to find its most similar products

  return: none
  """

  original = load_img(img, target_size =(224, 224))

  closest_imgs = df[img].sort_values(ascending = False)[1:5+1].index
  closest_imgs_scores = df[img].sort_values(ascending=False)[1:5+1]

  storage = []

  for i in range(len(closest_imgs)):
      original = load_img(closest_imgs[i], target_size = (224, 224))
      storage.append(original)
      #plt.imshow(original)
      #plt.show()
      #print("similarity score : ",closest_imgs_scores[i])
      #print("\n\n")

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


#test = recommended_outfit(files[20])

#def test2(a):
#    for i in test:
#        plt.imshow(i)
#        plt.show()

#test2(test)