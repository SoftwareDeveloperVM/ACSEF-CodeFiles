import numpy as np
import cv2 as cv
import time
import datetime
import os
import math

mode_select = input("Chose whether to record (X, Y) or to record (Z): ")
total_data_logs = []
cap = cv.VideoCapture(0)


def distance_calc(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

time.sleep(1)
ret, frame = cap.read()
bbox = cv.selectROI('select', frame, False)

x, y, w, h = bbox

roi = frame[y:y + h, x:x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

record_x = 0
record_y = 0

while (1):
    ret, frame = cap.read()
    complete_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cv.putText(frame, complete_time, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv.meanShift(dst, bbox, term_crit)

        x, y, w, h = track_window
        previous_x = record_x
        previous_y = record_y
        record_x = x + 0.5 * w
        record_y = y + 0.5 * h
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv.imshow('gfg', img2)
        if os.path.exists("images/" + str(current_date)):
            cv.imwrite("images/" + str(current_date) + "/" + str(current_time) + ".png", frame)
        else:
            os.mkdir("images/" + str(current_date))
            cv.imwrite("images/" + str(current_date) + "/" + str(current_time) + ".png", frame)
        if mode_select == "(X, Y)":
            print("\033[1;32;40m\n")

            print("Screenshot taken @ " + str(complete_time) + " with (X, Y) coordinates (" + str(record_x) + ", " + str(record_y) + ")")

            displacement = distance_calc(record_x, record_y, previous_x, previous_y)
            print("Displacement of " + str(displacement) + " units from the last image.")

            data = "Screenshot taken @ " + str(complete_time) + " with (X, Y) coordinates (" + str(record_x) + ", " + str(record_y) + ") with a " + "displacement of " + str(displacement) + " units from the last image."
            total_data_logs.append(data)
        elif mode_select == "(Z)":
            print("\033[1;34;40m \n")

            print("Screenshot taken @ " + str(complete_time) + " with (Z) coordinates (" + str(record_x) + ")")

            displacement = distance_calc(record_x, record_y, previous_x, previous_y)
            print("Displacement of " + str(displacement) + " units from the last image.")
            data = "Screenshot taken @ " + str(complete_time) + " with (Z) coordinates (" + str(record_x) + ") with a " + "displacement of " + str(displacement) + " units from the last image."
            total_data_logs.append(data)

        # print(record_x, previous_x, record_y, previous_y)

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

for val in total_data_logs:
    print(val)
