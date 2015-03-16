import datetime
import Config
from matplotlib import pyplot as plt
import cv2
import numpy as np
from Characteristic import ImagePart, Channel

from os.path import join

class Result:
    def __init__(self, state, image):
        self.__state = state
        self.__image = image
    def state(self):
        return self.__state
    def image(self):
        return self.__image



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

from Tools import validateType, merge_two_dicts

class HistoImage:
    __hsv = {
        Channel.HSV_H : 0,
        Channel.HSV_S : 1,
        Channel.HSV_V : 2,
    }
    __rgb = {
        Channel.RGB_R : 0,
        Channel.RGB_G : 1,
        Channel.RGB_B : 2,
    }
    __index = merge_two_dicts(__rgb, __hsv)
    def __init__(self, image):
        self.__image = image
        self.__hsvImage = None
        self.__histograms = {}
        self.__means = {}
        self.__standardDeviations = {}
    def histogram(self, channel):
        validateType(channel, Channel, "channel")
        if not channel in self.__histograms:
            if channel in (Channel.HSV_H, Channel.HSV_S, Channel.HSV_V):
                imageBase = self.imageHsv()
            else:
                imageBase = self.__image
            histogram = cv2.calcHist([imageBase],[self.__index[channel]],None,[256],[0,256])
            self.__histograms[channel] = histogram
            return histogram
        return self.__histograms[channel]
    def __calcMean(self, channel):
        if channel in self.__hsv:
            imageBase = self.imageHsv()
            colors = self.__hsv
        else:
            imageBase = self.__image
            colors = self.__rgb

        means, standardDeviations = cv2.meanStdDev(imageBase)
        for i, c in enumerate(colors):
            self.__means[c] = means[i][0]
            self.__standardDeviations[c] = standardDeviations[i][0]

    def mean(self, channel):
        validateType(channel, Channel, "channel")
        if not channel in self.__means:
            #TODO calc mean
            #self.__means[channel] = np.mean(self.histogram(channel))
            self.__calcMean(channel)
        return self.__means[channel]
    def standardDeviation(self, channel):
        validateType(channel, Channel, "channel")
        if not channel in self.__standardDeviations:
            #TODO calc standardDeviation
            self.__calcMean(channel)
            #self.__standardDeviations[channel] = np.std(self.histogram(channel))
        return self.__standardDeviations[channel]


    def image(self):
        return self.__image
    def imageHsv(self):
        if self.__hsvImage is None:
            self.__hsvImage = cv2.cvtColor(self.__image, cv2.COLOR_BGR2HSV)
        return self.__hsvImage

class ImageSplitter:
    def __init__(self, image):
        self.__image = image
        validateType(image, Image, "image")
        self.__cv2image = cv2.imread(image.fullPath())
        self.__images = {}
    def getImage(self, imagePart):
        validateType(imagePart, ImagePart, "imagePart")
        height, width  = self.__cv2image.shape[:2]
        webcam = self.__image.webcam()
        skyLeft = webcam.skyLeft()
        skyRight = webcam.skyRight()
        top = webcam.ignoreTop()
        bottom = webcam.ignoreBottom() if webcam.ignoreBottom() != 0 else height
        if not imagePart in self.__images:
            if imagePart == ImagePart.ALL:
                pts1 = np.float32([[0,top],[width,top],[0,bottom],[width,bottom]])
                pts2 = np.float32([[0,0],[width,0],[0,bottom],[width,bottom]])
                M = cv2.getPerspectiveTransform(pts1,pts2)
                all = HistoImage(cv2.warpPerspective(self.__cv2image,M,(width,bottom -top)))
                self.__images[imagePart] = all
                return all
            elif imagePart == ImagePart.SKY:
                maxSkyHeight = max(skyLeft, skyRight)
                bottomSky = maxSkyHeight - top
                print("top %d, bot %d" %(top, bottom))
                print("skyLeft(%d), skyRight(%d), maxSkyHeight(%d)" % (skyLeft, skyRight, maxSkyHeight))
                pts1 = np.float32([[0,top],[width,top],[0,skyLeft],[width,skyRight]])
                pts2 = np.float32([[0,0],[width,0],[0,bottomSky],[width,bottomSky]])
                M = cv2.getPerspectiveTransform(pts1,pts2)
                sky = HistoImage(cv2.warpPerspective(self.__cv2image,M,(width,bottomSky)))
                self.__images[imagePart] = sky
                return sky
            elif imagePart == ImagePart.GROUND:
                topGround = min(skyLeft, skyRight)
                bottomGround = bottom
                heightGround = bottomGround - topGround
                print("topGround(%d), bottomGround(%d), heightGround(%d)" % (topGround, bottomGround, heightGround))
                pts1 = np.float32([[0,skyLeft],[width,skyRight],[0,bottomGround],[width,bottomGround]])
                pts2 = np.float32([[0,0],[width,0],[0,heightGround],[width,heightGround]])
                M = cv2.getPerspectiveTransform(pts1,pts2)
                ground = HistoImage(cv2.warpPerspective(self.__cv2image,M,(width,heightGround)))
                self.__images[imagePart] = ground
                return ground
            raise ValueError("Type %s unknow" % repr(type))
        return self.__images[imagePart]


def plotImageColors(splitter, imagePart):
    validateType(splitter, ImageSplitter, "splitter")
    validateType(imagePart, ImagePart, "imagePart")
    colors = (
        (Channel.RGB_R, 'r'),
        (Channel.RGB_G, 'g'),
        (Channel.RGB_B, 'b'),
        (Channel.HSV_H, 'c'),
        (Channel.HSV_S, 'm'),
        (Channel.HSV_V, 'y'),
    )

    for channel, color in colors:
        plt.plot(splitter.getImage(imagePart).histogram(channel),color = color)
        plt.xlim([0,256])
    plt.show()

files = Config.filesInFolder(Config.pathImages, True)
images = [Image(f) for f in files][:24]



results = []

for image in [i for i in images if i.webcam().name()=="LSGC_east" and i.date().hour == 13]:
    splitter = ImageSplitter(image)
    # img = cv2.imread(image.fullPath())
    # webcam = image.webcam()
    # height, width  = img.shape[:2]
    # print("%d x %d" % (height, width))
    #
    # cv2.imshow("ori" + repr(image), img)
    # bottom = webcam.ignoreBottom() if webcam.ignoreBottom() != 0 else height
    # top = webcam.ignoreTop()
    # skyLeft = webcam.skyLeft()
    # skyRight = webcam.skyRight()
    # maxSkyHeight = max(skyLeft, skyRight)
    # bottomSky = maxSkyHeight - top
    # print("top %d, bot %d" %(top, bottom))
    # print("skyLeft(%d), skyRight(%d), maxSkyHeight(%d)" % (skyLeft, skyRight, maxSkyHeight))
    # pts1 = np.float32([[0,top],[width,top],[0,skyLeft],[width,skyRight]])
    # pts2 = np.float32([[0,0],[width,0],[0,bottomSky],[width,bottomSky]])
    # M = cv2.getPerspectiveTransform(pts1,pts2)
    # sky = cv2.warpPerspective(img,M,(width,bottomSky))
    # cv2.imshow("sky" + repr(image), sky)
    #
    # topGround = min(skyLeft, skyRight)
    # bottomGround = bottom
    # heightGround = bottomGround - topGround
    # print("topGround(%d), bottomGround(%d), heightGround(%d)" % (topGround, bottomGround, heightGround))
    # pts1 = np.float32([[0,skyLeft],[width,skyRight],[0,bottomGround],[width,bottomGround]])
    # pts2 = np.float32([[0,0],[width,0],[0,heightGround],[width,heightGround]])
    # M = cv2.getPerspectiveTransform(pts1,pts2)
    # ground = cv2.warpPerspective(img,M,(width,heightGround))
    # cv2.imshow("ground" + repr(image), ground)


    #hsvSky = cv2.cvtColor(sky,cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsvSky" + repr(image), hsvSky)


    # for imagePart in ImagePart:
    #     img = splitter.getImage(imagePart).image()
    #     print(repr(img))
    #     cv2.imshow(repr(imagePart), img)

    img = splitter.getImage(ImagePart.SKY)
    for channel in Channel:
        print("%s mean              = %s" %(channel, repr(img.mean(channel))))
        print("%s standardDeviation = %s" %(channel, repr(img.standardDeviation(channel))))


    plotImageColors(splitter, ImagePart.SKY)
    plotImageColors(splitter, ImagePart.GROUND)

    # hsvSky = splitter.getImage(ImagePart.SKY).imageHsv()
    # color = ('r','g','b')
    # for i, col in enumerate(color):
    #     #if i != 0 : break
    #     print("i = %d" % i)
    #     histr = cv2.calcHist([hsvSky],[i],None,[256],[0,256])
    #     print(type(histr))
    #     print(len(histr))
    #     # history[col] = histr
    #     print(histr)
    #     print(np.amax(histr))
    #     print(np.nanargmax(histr))
    #     #TODO Vincent equart type et moyenne sur histr
    #     plt.plot(histr,color = col)
    #     plt.xlim([0,256])
    #     #for i, val in enumerate(histr):
    #     #    print("%d = %d" % (i, val))
    # plt.show()


cv2.waitKey()

