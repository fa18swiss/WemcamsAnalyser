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
    Light_cloudy = 4


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
    def state(self):
        return self.__state
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
#Attention, H : [0, 180]
characteristics = (
    Characteristic("Night", Channel.HSV_V, ImagePart.SKY, State.Night, 10, 10, 3, 3),
    Characteristic("Night-sat", Channel.HSV_S, ImagePart.SKY, State.Night, 0, 1, 0, 1),

    Characteristic("Blue", Channel.HSV_H, ImagePart.SKY, State.Sun, 120, 25, 12, 12),

    Characteristic("Light-sun", Channel.HSV_V, ImagePart.SKY, State.Sun, 238, 17, 20, 20),

    Characteristic("claudy", Channel.HSV_S, ImagePart.SKY, State.Cloudy, 1, 1, 1, 1),

    Characteristic("claudy-foggy", Channel.HSV_S, ImagePart.SKY, State.Cloudy, 35, 5, None, None),

    Characteristic("gray", Channel.HSV_H, ImagePart.SKY, State.Cloudy, None, None, 36, 6),

    Characteristic("light-cloudy", Channel.HSV_S, ImagePart.SKY, State.Light_cloudy, 230, 10, 20, 15),

)
