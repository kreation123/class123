import cv2
import numpy as np
import pandas as pd
from pandas.core.window import rolling
import seaborn  as sb
import matplotlib.pyplot as mlp
from sklearn.datasets import fetch_openml 
from PIL import Image 
import PIL.ImageOps
import os,time,ssl
import LogisticRegression

if(not os.environ.get('Pythonhtpps','')and get attr(ssl,'_creat_unvired_context','')):
    ssl._create_default_https_context_

X,y = fetch_openml('mnist_784',version = 1 , return_X_y = Ture)
print(pd.Series(y).value_counts())
classes = ['0','1','2','3','4','5','6','7','8','9']
nclasses  = len(classes)
X_train,X_text,y_train,y_text = train_text_split(x,y,randomstae  = 9)
Xtrainscale = X_train/255
testtrainscale = X_train/255
capture = cv2.VideoCapture(0)
while(True):
    try:
        return,frame = cap.read()
        height,width = gray.shap
        upperleft =(init(width/2-50),init(hight/2-50))
        bottomright = (inti(width/2-50),init(hight/2+50))
        cv2.rectangle(gray,upperleft,bottmeright,(0,255,0),2)
        roi=grayuperleft,upperleft,bottemright
        PIL= image.fromarray(roi)
        pixplfiler=20 