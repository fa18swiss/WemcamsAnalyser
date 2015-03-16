from Tools import validateType
try:
    from enum import Enum
except:
    print("Module eunm not found, please download and install from https://pypi.python.org/pypi/enum34")
    import sys
    sys.exit(-1)


class ImagePart(Enum):
    ALL = 0
    SKY = 16
    GROUND = 32

class Channel(Enum):
    RGB_R = 1
    RGB_G = 2
    RGB_B = 3
    HSV_H = 4
    HSV_S = 5
    HSV_V = 6

class State(Enum):
    Unknown = 0
    Night = 1
    Sun = 2
    Cloudy = 3


#todo jules ajout equart type
class Characteristic:
    def __init__(self, name, channel, imagePart, state, mean, dMean, standardDeviation, dStandardDeviation):
        self.__name = name
        self.__channel = channel
        self.__imagePart = imagePart
        self.__state = state
        self.__mean = mean
        self.__dMean = dMean
        self.__standardDeviation = standardDeviation
        self.__dStandardDeviation = dStandardDeviation
        validateType(channel, Channel, "channel")
        validateType(imagePart, ImagePart, "imagePart")
        validateType(state, State, "state")
        validateType(mean, (float, int, type(None)), "mean")
        validateType(dMean, (float, int, type(None)), "dMean")
        validateType(standardDeviation, (float, int, type(None)), "standardDeviation")
        validateType(dStandardDeviation, (float, int, type(None)), "dStandardDeviation")
    def name(self):
        return self.__name
    def channel(self):
        return self.__channel
    def imagePart(self):
        return self.__imagePart
    def mean(self):
        return self.__mean
    def dMean(self):
        return self.__dMean
    def standardDeviation(self):
        return self.__standardDeviation
    def dStandardDeviation(self):
        return self.__dStandardDeviation

characteristics = (
    Characteristic("Blue", Channel.HSV_H, ImagePart.SKY, State.Sun, 1, 1.1, 0, None)
)

