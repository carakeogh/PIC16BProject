# PIC16B Project

**Group Name:** The Drip Gurus <br>
**Project Topic:** Outfit recommendation webapp <br>
**Group Members:** Cara Keogh, Patrick Wang, Yu-Hsin Huang <br>

## Introduction
This project aims to address the problem of people not being able to find their outfit preferences. The overall approach to accomplishing this task is to randomly generate outfits based on a large image dataset of clothes and accessories, get user feedback on the outfits, and ultimately produce an outfit recommendation for the user based on their style preferences.

## How Our Webapp Works
Our program is delivered in the form of an online webapp.
First, when users get into our webapp, they will see an introductory Drip Gurus Website that provides a link for users to go to the homepage of our program. The homepage then asks for users' names and asks whether users want to enter the outfit recommender program. If users show their intention to use the outfit recommender system, a welcoming text followed by a link to the recommender system will be given. Otherwise, users will be led to the introductory page. Once the users reach the recommender system page, they will first be asked to specify what type of outfit (Topwear, Bottomwear, Shoes, Belts, Socks, and Dress) they want the program to recommend. Next, our program will randomly generate five images according to the users' choice of style, and ask them which image fits their preference the most. After selecting the users' most preferred image, five similar outfit images based on their choice will be displayed to give them outfit recommendations.

## How to Access Our Webapp
*Please make sure you have all packages and flask installed in your local environment before running our webapp.* <br>
1. Fork this repository to your local device. 
2. Activate your local environment by running 'conda activate [environment]' in terminal. 
3. Run 'export FLASK_ENV=development; flask run' to get the link for our webapp on your local device.