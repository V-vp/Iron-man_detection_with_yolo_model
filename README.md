![capture](https://user-images.githubusercontent.com/22338553/36064105-f8868f5c-0eab-11e8-8b8d-aa86e37dd5e6.JPG)

Trained a YOLO model to detect Iron-man ....Just for Fun..
<p>Read more about YOLO  : <a href="https://arxiv.org/pdf/1506.02640.pdf">Paper 1</a>, <a href="https://arxiv.org/pdf/1612.08242.pdf">Paper 2</a> and <a href="https://pjreddie.com/darknet/yolo/">here.</a></p>
<p>Before trying it on your local machine please clone <a href = "https://github.com/thtrieu/darkflow.git">darkflow</a> Repo and Install all dependencies.</p>
<p>Then download these to weight files <a href = "https://drive.google.com/open?id=19QoNoUW8E4YulIxU-sSALO8V5_P0tipv">weight1</a> & <a href = "https://drive.google.com/open?id=1xIjebZI3DzTQZkHZ5cXORCe2vxQBHL5K">weight2</a>, and put it in ckpt folder.</p>
<p>I trained model with just somewhere around 500 images. So please set thresold value to 0.1. :) </p>
<p>To parse a Video file use this Command:</p>
      flow --model cfg/tiny-yolo-voc-1c.cfg --load 750 --demo ironman.mp4 --gpu 1.0 --saveVideo
<p></p>
<p>I will add to other avengers like Hulk, Thor, Captain America to it  later..</p>
<p>Thank you For Visiting....:)</p>
