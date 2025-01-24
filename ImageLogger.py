import cv2
import datetime
import time
import os

scr_val = 0
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
DesiredImageCount = 100
flag = False

while True:
    retval, video = camera.read()
    complete_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cv2.putText(video, complete_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    if DesiredImageCount != 0:
        time.sleep(1)
        scr_val += 1
        if os.path.exists("images/"+str(current_date)):
            cv2.imwrite("images/"+str(current_date)+"/"+str(current_time)+".png",video)
        else:
            os.mkdir("images/" + str(current_date))
            cv2.imwrite("images/" + str(current_date) + "/" + str(current_time) + ".png", video)
        print("Screenshot taken")
        DesiredImageCount -= 1
    else:
        break

camera.release()
cv2.destroyAllWindows()
