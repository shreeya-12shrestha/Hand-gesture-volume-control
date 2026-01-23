import cv2
import mediapipe as mp #google library used for real-time AI vision tasks like handtracking in this case
import pyautogui #can control computer directly using python
import math
x1=0 #x1,y1 is index finger tip
y1=0
x2=0 #x2,y2 is thumbfinger tip
y2=0
webcam=cv2.VideoCapture(0)
my_hands= mp.solutions.hands.Hands() #can capture our hands
drawing_utils= mp.solutions.drawing_utils #drawing_utils: draw dots & connections on hand
while True:
    _,image=webcam.read()
    image=cv2.flip(image,1) #flipping horizontally
    frame_height, frame_width, _=image.shape
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output= my_hands.process(rgb_image) #process the hand
    hands= output.multi_hand_landmarks #collect all the hands, it contains 21 landmark per hand
    if hands: #if hand is detected
        for hand in hands: #works even if two hands are present
            drawing_utils.draw_landmarks(image,hand) #for each hand draw the landmarks
            landmarks=hand.landmark
            for id, landmark in enumerate (landmarks): #id= landmark number (0-20)
                x=int (landmark.x *frame_width) #convert landmark to pixel coordinates
                y=int (landmark.y *frame_height)
                if id==8: #id =8 is recognize forefinger
                    cv2.circle(img=image, center=(x,y),radius=8,color=(0,255,255),thickness=3)
                    x1=x
                    y1=y
                if id==4: #id =4 is recognize thumbfinger
                    cv2.circle(img=image, center=(x,y),radius=8,color=(0,0,255),thickness=3)
                    x2=x
                    y2=y
        dist= (((x2-x1)**2)+((y2-y1)**2))**0.5//4
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5) #drawing lines betn forefinger and thumbfinger
        if dist>50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")
    cv2.imshow("Volume Control",image)
    key=cv2.waitKey(1)
    if key==27:
        break
webcam.release
cv2.destroyAllWindows()