import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def CT_scan(image , sav_path ,extention):


    def nothing(x):
        pass


    cv2.namedWindow('tracking')
    cv2.createTrackbar('lh','tracking',0,255,nothing)
    cv2.createTrackbar('ls','tracking',0,255,nothing)
    cv2.createTrackbar('lv','tracking',50,255,nothing)

    cv2.createTrackbar('uh','tracking',255,255,nothing)
    cv2.createTrackbar('us','tracking',255,255,nothing)
    cv2.createTrackbar('uv','tracking',70,255,nothing)

    while True:

        img1 = cv2.imread(image)
        #img1 = cv2.resize(img1,(500,500))
        lh = cv2.getTrackbarPos('lh','tracking')
        ls = cv2.getTrackbarPos('ls' , 'tracking')
        lv = cv2.getTrackbarPos('lv' , 'tracking')

        uh = cv2.getTrackbarPos('uh' , 'tracking')
        us = cv2.getTrackbarPos('us' , 'tracking')
        uv = cv2.getTrackbarPos('uv' , 'tracking')

        hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
        lower = np.array([lh,ls,lv])
        higher = np.array([uh,us,uv])
        mask = cv2.inRange(hsv,lower,higher)
        res = cv2.bitwise_or(img1,img1,mask=mask)

        gry_image = cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)
        ret , thresh = cv2.threshold(gry_image , 5,5,20)
        contors , har = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)


        cv2.drawContours(img1 ,contors, -1 , (255,255,0) , 1 )
        cv2.drawContours(res, contors, -1, (0, 0, 255), 1)
        print(len(contors))
        print(contors[0][0][0][1])
        cv2.imshow('covid' , img1)
        cv2.imshow('the mask' , mask)
        cv2.imshow('resulte' , res)
        detection = plt.imshow(res , 'CMRmap')
        print(detection) #print(len(contors))
        #print(contors[0][0][0][1])
        # cv2.imshow('covid' , img1)
        # cv2.imshow('the mask' , mask)
        #cv2.imshow('resulte' , res)
        #detection = plt.imshow(res , 'CMRmap')
        #print(detection)
        #plt.show()
        plt.show()


        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break


    cv2.destroyAllWindows()
    cv2.imwrite(sav_path + extention, res)
    return image , sav_path ,extention

import os
import glob

path = ('data set/test/Covid/*.*')
new_path = ('data set/test/New_Covid')
count = 0




CT_scan()