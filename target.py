# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JB-Q9vV1Cx5fsbhX1cTT3cXbn0Ip40Du
"""

from matplotlib import pyplot as plt

import cv2

image = cv2.imread("man.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

model = cv2.CascadeClassifier("model.xml")

face = model.detectMultiScale(image=image, scaleFactor=1.2, minNeighbors=5, minSize=(30,30))

x = face[0][0]
y = face[0][1]
a = face[0][2]
b = face[0][3]

image = cv2.rectangle(image, (x,y), (x + a, y + b), (0,255,0), 3)

plt.imshow(image)

from matplotlib import pyplot as plt

import cv2

image = cv2.imread("mamad.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

model = cv2.CascadeClassifier("model.xml")

face = model.detectMultiScale(image=image, scaleFactor=1.2, minNeighbors=5, minSize=(30,30))

x = face[0][0]
y = face[0][1]
a = face[0][2]
b = face[0][3]

image = cv2.rectangle(image, (x,y), (x + a, y + b), (0,255,0), 3)

plt.imshow(image)