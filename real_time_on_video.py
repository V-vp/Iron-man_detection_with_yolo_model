import tensorflow as tf
import matplotlib
import numpy as np
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import time

options = {
    'model':'cfg/tiny-yolo-voc-1c.cfg',
    'load':750,
    'threshold':0.15,
    'gpu':0.7
}

tfnet = TFNet(options)

video = cv2.VideoCapture('ironman.mp4')

colors = [tuple(255*np.random.rand(3)) for i in range(5)]

while(video.isOpened()):
    stime = time.time()
    ret,frame = video.read()
    results = tfnet.return_predict(frame)
    if ret:
        for color,result in zip(colors,results):
            #print(result)
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            frame = cv2.rectangle(frame, tl, br, (0, 255, 0), 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('frame',frame)
        print('FPS{:.1f}'.format(1/(time.time()-stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        video.release()
        cv2.destroyAllWindows()
        break



