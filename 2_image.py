import tensorflow as tf
import matplotlib
import numpy
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

#%config InlineBackend.figure_format = 'avg'

options = {
    'model':'cfg/tiny-yolo-voc-1c.cfg',
    'load':750,
    'threshold':0.1,
    #'gpu':1.0
}

tfnet = TFNet(options)

img = cv2.imread('iron2.png',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(img)
#print(result)
tl = (result[0]['topleft']['x'],result[0]['topleft']['y'])
br = (result[0]['bottomright']['x'],result[0]['bottomright']['y'])
label = result[0]['label']

#confidence = result[0]['confidence']
#text = '{} : {:.0f}%'.format(label,confidence*100)
img = cv2.rectangle(img,tl,br,(0,255,0),7)
img = cv2.putText(img,label,tl,cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#img = cv2.putText(img,label,tl,cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

plt.imshow(img)
plt.show()