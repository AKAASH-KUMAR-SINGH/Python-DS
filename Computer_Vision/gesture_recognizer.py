import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import cv2

path='Computer_Vision\gesture_recognizer.gesture_recognizer.task'

import mediapipe as mp

BaseOptions = mp.tasks.GestureRecognizer
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

result=[]
# Create a gesture instance with the live stream mode:
def process_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))
    result.append(result)
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with GestureRecognizer.create_from_options(options) as recognition:
    print("Gesture recognizer model loaded")
    cam=cv2.VideoCapture(0)
    while cam.isOpened():
        state,image=cam.read()
        if not state : break
        mp_image=mp_Image(image_format=mp.ImageFormat.SRGB,data=image) 
        ts=int(time.time()*1000)

# 
h,w,_=image.shape
if results:
    if len(results)>0:
        cv2.putText(image,"Gesture recognised",
        (40,40),cv2.FONT_HERSHEY_COMPLEX_SMALL,.5,(0,0,255),1)
        result=result.pop()
        gesture,hand="",""
        if len(result.gesture)>0:
            gesture=result.gestures[0][0].category_name
        if len(result.handedness)>0:
            hand=result.handedness[0][0].category_name

        cv2.rectangle(image, (0,h-80),(w,h),(0,0,0),-1)
        if gesture:
            cv2.putText(image,f'{hand}-{gesture}',
            (40,h-40),cv2.FONT_HERSHEY_COMPLEX,
            1,(0,255,255),1)
        index_pos=None
        for landmark in result.hand_landmarks:
            for i in landmark:
                nx,ny=i.x,i.y
                x,y=int(nx*w),int(ny*h) #normalised to pixel size
                print('index finger at',x,y)
                cv2.circle(image,(x,y),5,(0,255,0),-1)


cv2.imshow('MediaPipe Gesture Recognition',image)
key=cv2.waitKey(10)
if key==27:break 