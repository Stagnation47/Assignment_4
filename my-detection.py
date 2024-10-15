#from jetson.inference import detectNet
#from jetson.utils import videoSource, videoOutput
#from jetson.utils import loadImage, saveImage
import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

image_path = "/home/nvidia/jetson-inference/data/images/airplane_0.jpg"
#image_path = loadImage("image.jpg")
img = jetson.utils.loadImage(image_path)
#detections = net.Detect(img)

#if  img is True:

detections = net.Detect(img)
for detection in detections:
    #class_id = detection.ClassID
    #confidence = detection.Confidence
    #left,top,right,bottom = detection.Left, detection.Top, detection.Right, detection.Bottom 


   # print(net.GetClassDesc(detection.ClassID))
    print(detection)
  
#saveImage("Image_with_detections.jpg", image)

#camera = videoSource("/dev/video0") #'/dev/video0'for V4L2
#display = videoOutput("display://0") #'my_video.mp4'for file

#while display.IsStreaming():
    
    #img = camera.Capture()

   # if img is None: #capture timeout
     #   continue
    
    #detections = net.Detect(img) 
    #print(detections)

   # display.Render(img)
   #display.SetStatus("Object Detection | Network{:.0f}FPS".format(net.GetNetworkFPS()))
