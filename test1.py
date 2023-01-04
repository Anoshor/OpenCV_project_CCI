import cv2
import mediapipe as mp
import pyautogui
import math
import pywhatkit

cap=cv2.VideoCapture(0)
detector=mp.solutions.hands.Hands()
utils=mp.solutions.drawing_utils

s_width,s_height=pyautogui.size()
x1=0
y1=0


while True:
    success, img=cap.read()
    img=cv2.flip(img,1)
    img_height,img_width,c=img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output=detector.process(imgRGB)
    hands=output.multi_hand_landmarks

    listh=[]
    if hands:
        for hand in hands:
            utils.draw_landmarks(img,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*img_width)
                y=int(landmark.y*img_height)
                listh.append([id,x,y])
            if len(listh)!=0:
                # print(listh[4],listh[8])
                a1, b1=listh[8][1], listh[8][2]
                a2, b2=listh[12][1], listh[12][2]
                a3, b3=listh[16][1], listh[16][2]
                a4, b4=listh[4][1], listh[4][2]
                cv2.circle(img=img, center=(a1, b1), radius=11, color=(255, 0, 0))
                cv2.circle(img=img, center=(a2, b2), radius=11, color=(255, 0, 0))
                cv2.circle(img=img, center=(a3, b3), radius=11, color=(255, 0, 0))
                # x1 = s_width / img_width * listh[8][1]
                # y1 = s_height / img_height * listh[8][2]
                # x2 = s_width / img_width * listh[4][1]
                # y2 = s_height / img_height * listh[4][2]
                cv2.line(img, (a1, b1), (a2, b2), (0, 255, 0), 3)
                cv2.line(img, (a2, b2), (a3, b3), (0, 255, 200), 3)
                cv2.line(img, (a1, b1), (a4, b4), (0, 0, 0), 3)
                length1=int(math.hypot(a2-a1,b2-b1))
                length2 = int(math.hypot(a3 - a2, b3 - b2))
                length3 = int(math.hypot(a1 - a4, b1 - b4))
                print(length1,length2,length3)
                # CREATE a 'W' with your index,middle,ring finger to send a whatsapp text !!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!
                # bring your thumb and index close to end the program
                if(length1<=80 and length1>=60 and length2<=80 and length2>=60):
                    # code for sending a whatsapp text
                    # pywhatkit.sendwhatmsg_to_group_instantly("nobody cares", "yoo! I can send text on group")
                    # pywhatkit.sendwhats_image("nobody cares", "C:/Users/anosh/Downloads/feelfunny.jpg", "heh")
                    #print("enter number: ")
                    nums=input("enter number : ")
                    # #print("enter text: ")
                    texts=input("enter text : ")
                    # #print("enter hrs, mins: ")
                    hrs,mins=input("enter hrs, mins: ").split()
                    pywhatkit.sendwhatmsg(nums, texts, int(hrs), int(mins))
                    # pywhatkit.sendwhatmsg('+91XXXXXXXXXX','Hello xxx, blah blah',8,38)
                #code for virtual mouse click
                # if id==8:
                #     cv2.circle(img=img,center=(x,y),radius=11,color=(255,0,0))
                #     x1=s_width/img_width*x
                #     y1=s_height/img_height*y
                #     print(id,x1,y1)
                #     # pyautogui.moveTo(x1,y1)
                # if id==4:
                #     cv2.circle(img=img,center=(x,y),radius=11,color=(255,0,255))
                #     x2=s_width/img_width*x
                #     y2=s_height/img_height*y
                    # if abs(y1-y2)<20:
                    #     pyautogui.click()
                    #     pyautogui.sleep(1)
                        # print('click')
                if length3 < 10:
                    exit()



    cv2.imshow("Image", img)
    cv2.waitKey(1)
