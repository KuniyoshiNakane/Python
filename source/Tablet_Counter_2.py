# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:46:31 2021

@author: Kuniyoshi Nakane
"""

import cv2
import numpy as np

# VideoCaptureオブジェクトを取得
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    
    if ret :
        blur = cv2.medianBlur(frame, 5)
        img = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.0, 20,
                                   param1=50, param2=37, minRadius=3, maxRadius=30)
        if not(circles is None) :
            circles = np.uint16(np.around(circles))
        
            if len(circles[0, :]) > 0:
                for i in circles[0, :]:
                    # 抽出した円を書き込み
                    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                    # 抽出した円の中心を書き込み
                    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
                    
                    cv2.putText(frame, '{} Tablets'.format(len(circles[0,:])), (0, 32), cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 0, 255))
        
        cv2.imshow('Detect Tablet', frame)
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

capture.release()
cv2.destroyAllWindows()
