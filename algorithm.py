from PIL import Image
import os
import matplotlib.pyplot as plt
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

def start(a):
    imgs_path = "/Users/wangp/OneDrive/Documents/GitHub/PIC16BProject/images/"

    imgs_model_width, imgs_model_height = 224, 224
    nb_closest_images = 5

    files = [imgs_path + x for x in os.listdir(imgs_path) if "jpg" in x]
    files=files[0:500]

    return files


from keras import models

def model(file):
    vgg_model = vgg16.VGG16(weights='imagenet')
    model = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)

    # run images through model
    importedImages = []

    for f in files:
        filename = f
        original = load_img(filename, target_size=(224, 224))
        numpy_image = img_to_array(original)
        image_batch = np.expand_dims(numpy_image, axis=0)
    
        importedImages.append(image_batch)
    
images = np.vstack(importedImages)

processed_imgs = preprocess_input(images.copy())

img_features = model.predict(processed_imgs)

cosSimilarities = cosine_similarity(img_features)
cos_similarities_df = pd.DataFrame(cosSimilarities, columns=files, index=files)

def recommended_outfit(img):
  """
  retrieve the most similar 5 products for the imputted image

  arguements:
  img: image that is going to be used to find its most similar products

  return: none
  """
  print("Original product:")

  original = load_img(img, target_size=(imgs_model_width, imgs_model_height))
  plt.imshow(original)
  plt.show()

  print("\n\nMost similar products:")

  closest_imgs = cos_similarities_df[img].sort_values(ascending=False)[1:nb_closest_images+1].index
  closest_imgs_scores = cos_similarities_df[img].sort_values(ascending=False)[1:nb_closest_images+1]

  storage = []

  for i in range(len(closest_imgs)):
      original = load_img(closest_imgs[i], target_size=(imgs_model_width, imgs_model_height))
      #plt.imshow(original)
      #plt.show()
      #print("similarity score : ",closest_imgs_scores[i])
      #print("\n\n")

  return storage

test = recommended_outfit(files[20])

def test2(a):
    for i in test:
        plt.imshow(i)
        plt.show()

test2(test)