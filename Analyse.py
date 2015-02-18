import datetime
import Config
from os.path import join

class Result:
    def __init__(self):
        #self.
        pass


class Image:
    def __init__(self, name):
        date = name[:15]
        self.__date = datetime.datetime.strptime(date, Config.dateFormat)
        webcam = name[16:].split(".")[0]
        self.__name = name
        self.__webcam = [w for w in Config.webcams if w.name() == webcam][0]
    def webcam(self):
        return self.__webcam
    def date(self):
        return self.__date
    def fullPath(self):
        return join(Config.pathImages, self.__name)
    def __repr__(self):
        return "Image path=%s, date=%s, webcam=%s" % (self.__name, self.__date, self.__webcam)




files = Config.filesInFolder(Config.pathImages, True)
images = [Image(f) for f in files][:24]

import cv2
import numpy as np

for image in [i for i in images if i.webcam().name()=="LSPL_east"]:
    img = cv2.imread(image.fullPath())
    webcam = image.webcam()
    height, width  = img.shape[:2]
    print("%d x %d" % (height, width))
    #crop = img[0:image.webcam().ignoreTop(), width:image.webcam().ignoreBottom()]
    #im[y1:y2, x1:x2]
    #crop = img[]
    cv2.imshow("ori" + repr(image), img)
    bottom = webcam.ignoreBottom() if webcam.ignoreBottom() != 0 else height
    top = webcam.ignoreTop()
    skyLeft = webcam.skyLeft()
    skyRight = webcam.skyRight()
    maxSkyHeight = max(skyLeft, skyRight)
    bottomSky = maxSkyHeight - top
    print("top %d, bot %d" %(top, bottom))
    print("skyLeft(%d), skyRight(%d), maxSkyHeight(%d)" % (skyLeft, skyRight, maxSkyHeight))
    #crop = img[webcam.ignoreTop():bottom, 0:width]
    #cv2.imshow("crop"+repr(image), crop)
    pts1 = np.float32([[0,top],[width,top],[0,skyLeft],[width,skyRight]])
    pts2 = np.float32([[0,0],[width,0],[0,bottomSky],[width,bottomSky]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    sky = cv2.warpPerspective(img,M,(width,bottomSky))
    cv2.imshow("sky" + repr(image), sky)

    topGround = min(skyLeft, skyRight)
    bottomGround = bottom
    heightGround = bottomGround - topGround
    print("topGround(%d), bottomGround(%d), heightGround(%d)" % (topGround, bottomGround, heightGround))
    pts1 = np.float32([[0,skyLeft],[width,skyRight],[0,bottomGround],[width,bottomGround]])
    pts2 = np.float32([[0,0],[width,0],[0,heightGround],[width,heightGround]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    ground = cv2.warpPerspective(img,M,(width,heightGround))
    cv2.imshow("ground" + repr(image), ground)

    #img.he

cv2.waitKey()