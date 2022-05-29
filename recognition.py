import app
import cv2
import numpy as np
from PIL import Image
import os
import time

tempid="temp"
count=0
def recog(names):

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')

    cascadePath = "Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)


    font = cv2.FONT_HERSHEY_SIMPLEX



    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    img_counter=0
    while True:
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 70):  #matched with recognised faces
                if id - 1>= len(names):
                    id = names[-1]
                else:
                    id = names[id - 1]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "Unrecognised"
                confidence = "  {0}%".format(round(100 - confidence))
            
            global tempid
            tempid = id
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
            if(tempid=="Unrecognised"):
                global count
                if(count < 1):
                    print(tempid)
                    img_name = "unknownPerson{}.jpg".format(img_counter)
                    cv2.imwrite(img_name, img)
                    img_counter+=1
                    app.send_email(img_name)
                    count=count+1

        
        ret, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result

        

        k = cv2.waitKey(40) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break


    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleaning up stuff")
    cam.release()
    cv2.destroyAllWindows()