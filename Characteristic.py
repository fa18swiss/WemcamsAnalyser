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
    Rain = 4
    Light_cloudy = 5
    Snow = 6


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
    #LSGC_east 1310
    Characteristic("Blue", Channel.HSV_H, ImagePart.SKY, State.Sun, 120, 10, 20, 10),
    #LSGC_west 1310
    Characteristic("Blue-sun", Channel.HSV_V, ImagePart.SKY, State.Sun, 230, 25, 30, 5),
    #LSPL_east 0850
    Characteristic("snow", Channel.HSV_S, ImagePart.SKY, State.Snow, 5, 5, 2, 2),
    #LSGC_west 0920
    Characteristic("snow-foggy", Channel.HSV_S, ImagePart.SKY, State.Snow, 0, 18, 25, 10),
    #LSGN_east 0720
    Characteristic("cloudy", Channel.HSV_H, ImagePart.SKY, State.Cloudy, 38, 10, 13, 10),
    #LSZQ_west 0440
    Characteristic("Night", Channel.HSV_V, ImagePart.SKY, State.Night, 10, 10, 3, 3),
    #LSGL_south 1350 TODO le soucis vient que lon ne peu pas differencier avec LSGC_west
    #Characteristic("ERROR", Channel.HSV_H, ImagePart.SKY, State.Sun, 17, 100, 4, 5),
    #StImier 1320
    Characteristic("snow-rain", Channel.HSV_V, ImagePart.SKY, State.Rain, 188, 10, 13, 2),
    #part2
    #LSPL_west
    Characteristic("cloudy", Channel.HSV_H, ImagePart.SKY, State.Cloudy, 56, 4, None, None),
    #LSPL_east
    Characteristic("light-cloudy", Channel.HSV_H, ImagePart.SKY, State.Light_cloudy, 80, 20, 0, 15),
    #LSPL_west
    Characteristic("cloudy", Channel.HSV_H, ImagePart.SKY, State.Cloudy, 90, 20, 0, 15),
    #LSZQ_west
    Characteristic("sun", Channel.HSV_H, ImagePart.SKY, State.Sun, 95, 10, None, None),
    #LSGL_north
    Characteristic("sun", Channel.HSV_H, ImagePart.SKY, State.Sun, 0, 10, None, None),




)

