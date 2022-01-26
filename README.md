# PIC16BProject

**Group Name:** The Drip Gurus
**Project Topic:** Outfit recommendation webapp
**Group Members:** Cara Keogh, Patrick Wang, Yu-Hsin Huang

## Abstract
This project aims to address the problem of people not being able to decide what to wear. Whether they don’t want to spend the time styling themselves or they aren’t sure what items work well together, our model will help them fully utilize their closet. The overall approach to accomplishing this task is to randomly generate outfits based on a large image dataset of clothes and accessories, get user feedback on the outfits, and ultimately produce an outfit recommendation for the user based on their style preferences.

## Planned Deliverables
We plan to deliver our program in the form of an online webapp.

Partial Success: 
We will consider our project to be partially successful if we can (1) create a model which identifies the user’s style preferences from the randomly generated outfits and (2) recommend an outfit from the images available in the dataset.

Full Success: 
We will consider our project to be fully successful if we can (1) create a model which identifies the user’s style preferences from the randomly generated outfits, (2) allow the user to upload pictures of their own clothes through the webapp, (3) use an algorithm to appropriately categorize the images provided by the user, and (4) recommend an outfit from the user-provided images. 

## Resources Required
We believe that the only resource we will need to complete our project is data. This is because training and testing data is required to build and implement our machine learning/image classification algorithms and recommendator system. Further, we plan to use datasets that contain a wide variety of images in clothes and accessories so that our application can account for more unique styles and clothing that might be less popular or prevalent in the world. 

Here are a few inks to some potential datasets that we plan to use:
- https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset
- https://www.kaggle.com/agrigorev/clothing-dataset-full
- https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html

## Tools and Skills Required
Since our entire program’s function is to categorize unique clothing items and recommend outfits accordingly, we will undoubtedly need some sort of image classification algorithm. Most of these algorithms use convoluted neural networks to assist them in accurately predicting unknown/new graphics. Additionally, we will need to implement some sort of program that outputs a visualization of recommended outfits to the user. However, before we can even implement these visualizations, we need to first design a machine learning algorithm that accurately predicts the user’s style preference based on their likes/dislikes of pre-generated outfits or on their own uploaded pictures. 

## What You Will Learn
On the technical side, our project will utilize image classification packages such as Keras. Then, we will learn the concept of convolutional neural networks to extract useful information from images. As for the recommender system, we will implement content-based filtering techniques to recognize the users’ preferred style, and suggest a similar outfit for the user. Moreover, we will develop our algorithm in a form of webapp, so we will utilize Flask to manage our dynamic web application. Additionally, since this is a group project, we will learn version control, which allows all of us to work simultaneously on the project. We will mainly collaborate and store our repository on Git. While working in groups, we can also learn some project management principles such as setting goals, creating a project timeline, distributing work, and so on.

## Risks
First, by achieving our full deliverable, the users will be able to upload their clothes and our algorithm will automatically match the outfits for the users. During this process, one potential risk would be that the algorithm is unable to recognize and categorize the clothes uploaded. This may be due to the clothes that are uploaded do not match any of the data we have, or the accuracy of the algorithm is not high enough to classify the clothes. Secondly, since our recommender system will be built based on the users’ selected preference, if the user does not have enough clothes that match his/her preference, the algorithm might not be able to suggest outfits properly. Since the sample size of choices is too small, the accuracy of the algorithm may be totally off.

## Ethics
Our whole program will be implemented as a web application. This comes with many benefits as well as limitations regarding accessibility to technology. The main goal of our program is to help individuals design personalized outfits based on their preferences and wardrobe. Therefore, people who have reliable access to technology and can upload pictures to the web can use and benefit from our application. Further, individuals who have many different articles of clothing or are just unsure of how to utilize their apparel to its highest potential will greatly benefit from our application. 

Because our program is reliant on the internet, the biggest group of people that will be harmed will be those without reliable access to tech. There isn’t any way for them to interact with our app since it lives on the web. Additionally, there are no limits to the number of clothing styles in the world. Anyone can create and establish their own style, which makes categorizing general styles pretty difficult. People who have clothings that aren’t reflected in the original training set of our algorithms will not get much out of our app since the classifications will not be accurate, thereby hindering the recommendations. 

Overall, a considerable portion of an individual’s spending is spent on apparel because it's essential; people will need to buy clothing at some point in their lives. Clothing offers a way for individuals to express themselves in countless ways, so it may be pretty difficult coming up with unique styles and figuring out what clothing items to purchase. Our application will address this issue and save users time and money that would have normally been spent on picking out the right clothes or deciding what to buy next. Furthermore, because our application will recommend personalized outfits for each user, there will be much less of an incentive to purchase from fast fashion brands. Instead of contributing to fast fashion due to lack of knowledge on what to purchase, users will now have a stronger idea of their next clothing item because they have a personalized outfit recommendation. With all the pros and the cons considered, we believe that our application will benefit society and make the world a better place!

## Tentative Timeline
Meet every Thursday at 8:30pm to recap week + plan for next week

**Week 3**
- Finish proposal
- Research on image classification
- Start cleaning data

**Week 4**
*1/27- Project Proposal due*
- Finish cleaning data
- Start classification
- Get basic webapp outline set up

**Week 5**
- Finish up Image classification
- Start building Recommendation system
- Start building out space for random image generation on webapp, like/dislike button for user to push

**Week 6**
*2/10- Project Update 1 Due*
- Continue working on recommendation system
- Finish space for random image generation on webapp

**Week 7**
*(Goal: Achieve Partial Success)*
- Finish recommendation system code for images that already exist in database

**Week 8**
*2/24- Project Update 2 Due*
- Add space on webapp for user to upload their pictures
- Begin adjusting recommendation system code for images that user uploads
- Begin building model to categorize images user uploads

**Week 9**
- Finish recommendation system code for images that user uploads
- Finish model to categorize images user uploads
- Put finishing touches on webapp

**Week 10**
*(Goal: Achieve Full Success)*
*3/9- Project Presentations Due*
- Finish blog post